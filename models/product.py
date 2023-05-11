from models.base_model import BaseModel


class Product(BaseModel):
    @staticmethod
    def add_product():

        """
        This method will add product to DB

        """
        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")
        product_description = input("Enter product description: ")
        category_id = input("Enter category id: ")
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO products (name, price, description, category_id) VALUES (%s, %s, %s, %s)',
                       (product_name, product_price, product_description, category_id))
        conn.commit()
        return "Product added successfully"

    @staticmethod
    def delete_product():
        """
        This method will delete product from DB
        """
        id = input("Enter product id to delete: ")
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = %s', (id,))
        conn.commit()
        return "Product deleted successfully"

    @staticmethod
    def see_all_products():
        """
        This method will see all products from DB
        """
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return "done!"

    @staticmethod
    def add_to_orders(product_id, user_id):
        """
        This method will add product to orders
        """
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO orders (product_id, user_id) VALUES (%s, %s)',
                       (product_id, user_id))
        conn.commit()
        return "The product has been purchased successfully"
    @staticmethod
    def search_by_name():
        """
        This method will search product by name
        """
        name = input("Enter product name: ")
        conn = BaseModel.cone_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products WHERE name = %s', (name,))
        rows = cursor.fetchall()
        # for row in rows:
        #     print(row)
        return rows[0][0]



    @staticmethod
    def select_by_category():
        """
        This method will select products by category
        """
        conn = BaseModel.cone_db()
        cursor = conn.cursor()

        # Fetch all categories from the "categories" table
        cursor.execute('SELECT * FROM categories')
        categories = cursor.fetchall()

        # Display available categories
        print("Available categories:")
        for category in categories:
            print(category[1])

        # Prompt the user to enter the category name
        name = input("Enter category: ")

        # Check if the entered category name exists in the "categories" table
        category_exists = False
        for category in categories:
            if category[1] == name:
                category_exists = True
                break

        if category_exists:
            # Fetch products based on the specified category name
            cursor.execute(
                'SELECT * FROM products JOIN categories ON products.category_id = categories.category_id WHERE categories.name = %s;',
                (name,)
            )
            rows = cursor.fetchall()

            if rows:
                for row in rows:
                    print(row)
            else:
                print("No products found in the specified category.")
        else:
            print("Invalid category name.")

        # Close the cursor and the database connection
        cursor.close()
        conn.close()


