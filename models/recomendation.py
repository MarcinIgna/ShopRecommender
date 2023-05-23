import pandas as pd
from sqlalchemy import create_engine
from sklearn.metrics.pairwise import cosine_similarity


def get_user_recommendations(user_id):
    top_n = 2 # Number of recommendations to return
    engine = create_engine('postgresql://postgres:qwertz@localhost:5432/machine_learning_1')

    # Fetch user-item interactions data from the database
    query = "SELECT * FROM user_item_matrix;"
    user_item_df = pd.read_sql(query, con=engine)

    # Aggregate the interactions using sum
    user_item_df = user_item_df.groupby(['user_id', 'product_id'])['interaction'].sum().reset_index()

    # Pivot the DataFrame to create the user-item matrix
    user_item_matrix = user_item_df.pivot(index='user_id', columns='product_id', values='interaction')
    user_item_matrix = user_item_matrix.fillna(0)

    # Calculate the similarity matrix between users
    similarity_matrix = cosine_similarity(user_item_matrix, user_item_matrix)
    similarity_df = pd.DataFrame(similarity_matrix, index=user_item_matrix.index, columns=user_item_matrix.index)

    # Get the similarity scores for the target user
    user_similarity_scores = similarity_df.loc[user_id]

    # Sort similarity scores in descending order and select top similar users
    similar_users = user_similarity_scores.sort_values(ascending=False).head(top_n)

    # Retrieve user-item interactions for similar users
    similar_users_interactions = user_item_matrix.loc[similar_users.index]

    # Calculate the sum of interactions for each item across similar users
    item_interaction_sums = similar_users_interactions.sum()

    # Remove items that the target user has already interacted with
    target_user_interactions = user_item_matrix.loc[user_id]
    item_interaction_sums = item_interaction_sums.drop(target_user_interactions[target_user_interactions > 0].index)

    # Sort recommendations based on interaction sums in descending order
    recommendations = item_interaction_sums.sort_values(ascending=False)

    # Fetch product IDs and names from the "products" table
    product_info_df = pd.read_sql("SELECT product_id, name FROM products;", con=engine)

    # Merge recommendations with product_info_df based on product_id
    recommendations_with_names = pd.DataFrame({'Product ID': recommendations.index})
    recommendations_with_names = pd.merge(recommendations_with_names, product_info_df, left_on='Product ID',
                                          right_on='product_id')

    # Select only the necessary columns (Product ID and name)
    recommendations_with_names = recommendations_with_names[['Product ID', 'name']]

    # Select the top N recommended items
    top_recommendations = recommendations_with_names.head(top_n)

    return top_recommendations


# Get recommendations for user with ID 1
# recommendations = get_user_recommendations(1)

# Print the recommendations without the index column
# print(recommendations.to_string(index=False))

