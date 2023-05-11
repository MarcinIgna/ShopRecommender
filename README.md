# ShopRecommender

A data-driven shopping recommendation algorithm powered by machine learning.

## Description

ShopRecommender is a machine learning-based algorithm designed to provide personalized shopping recommendations to users. It analyzes user interactions and preferences to suggest relevant products that match their interests.

The algorithm utilizes techniques such as collaborative filtering and cosine similarity to identify similar users and recommend products based on their past interactions. It leverages a dataset of user-item interactions and learns from patterns to make accurate recommendations.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/ShopRecommender.git`
2. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Ensure you have the necessary data files and database setup.
2. Run the main algorithm script: `python main.py`
3. Basic user is hardcoded, you can change it in `methods.user.py`.
4. The algorithm will provide a list of recommended products based on the user's preferences.

## Data Sources

The algorithm uses a dataset of user-item interactions, which includes user IDs, product IDs, and interaction data. This data is collected from PostgreSQL.

## Algorithms and Techniques

- Collaborative filtering: The algorithm identifies similar users based on their past interactions and recommends products that similar users have shown interest in.
- Cosine similarity: It calculates the cosine similarity between user vectors to measure the similarity between users and find the most similar ones.

## Results

The algorithm has been evaluated using various metrics such as precision, recall, and mean average precision. It has shown promising results in providing relevant and accurate shopping recommendations to users.


## Contact

For any questions or inquiries, please feel free to contact me.

Feel free to customize the sections and add any additional information that is relevant to your project.
