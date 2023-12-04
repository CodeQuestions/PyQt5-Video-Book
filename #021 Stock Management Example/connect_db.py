import sqlite3
from pathlib import Path


class DatabaseConnect:
    def __init__(self):
        # Database setup
        self.db_folder = "./db"
        self.db_path = f"{self.db_folder}/products_db.db"
        self.table_name = "product_master"
        self.connection = None
        self.cursor = None

        # Initialize the database
        self.init_database()

    def init_database(self):
        # Create necessary folder and database file if they don't exist
        folder_path = Path(self.db_folder)
        db_path = Path(self.db_path)

        if not folder_path.exists():
            folder_path.mkdir(parents=True)

        if not db_path.exists():
            with open(self.db_path, "w"):
                pass

        # Connect to the database and create the table if it doesnt exist
        self.connector()
        try:
            # Check if the table exists
            sql = f"SELECT name FROM sqlite_master WHERE type='table' and name='{self.table_name}'"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()

            if result:
                return
            else:
                # Create the table if it doesnt exist
                sql = f"""
                    CREATE TABLE '{self.table_name}' (
                    "product_name"	TEXT NOT NULL,
                    "cost"	NUMERIC,
                    "price"	NUMERIC,
                    "location"	INTEGER,
                    "reorder_level"	INTEGER,
                    "stock"	INTEGER DEFAULT 0,
                    PRIMARY KEY("product_name")
                    );                   
                    """
                self.cursor.execute(sql)
                # Commit changes to the database
                self.connection.commit()

        except Exception as e:
            self.connection.rollback()
            return e

        finally:
            # Close the cursor and connection
            self.cursor.close()
            self.connection.close()

    def connector(self):
        # Establish a connection to the SQLite database
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def common_update_execute(self, sql):
        # Execute common update SQL statements
        self.connector()
        try:
            self.cursor.execute(sql)
            # Commit changes to the database
            self.connection.commit()
        except Exception as e:
            # Rollback changes in case of an exception
            self.connection.rollback()
            return e
        finally:
            # Close the cursor and connection
            self.cursor.close()
            self.connection.close()

    def common_search_one_execute(self, sql):
        # Execute common search SQL statement for one result
        self.connector()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except Exception:
            return None
        finally:
            self.cursor.close()
            self.connection.close()

    def common_search_all_execute(self, sql):
        # Execute common search SQL statement for all results
        self.connector()
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception:
            return None
        finally:
            self.cursor.close()
            self.connection.close()

    def get_all_locations(self):
        # Retrieve distinct location form the table
        sql = f"SELECT DISTINCT location FROM {self.table_name};"
        result = self.common_search_all_execute(sql=sql)

        return result

    def add_new_product(self, **kwargs):
        # Insert a new product into the table
        column_name = tuple(kwargs.keys())
        values = tuple(kwargs.values())

        sql = f"INSERT INTO {self.table_name} {column_name} VALUES {values};"
        result = self.common_update_execute(sql=sql)

        return result

    def update_product(self, **kwargs):
        # Update product info in the table
        values = tuple(kwargs.values())

        sql = f""" UPDATE {self.table_name} SET 
                    cost={kwargs["cost"]}, 
                    price={kwargs["price"]}, 
                    location={kwargs["location"]}, 
                    reorder_level={kwargs["reorder_level"]}, 
                    stock={kwargs["stock"]}
                   WHERE product_name='{values[0]}';
            """

        result = self.common_update_execute(sql=sql)
        return result

    def get_data(self, search_flag="", product_name=""):
        """
            search_flag: ALL, IN_STOCK, RE_ORDER, NO_STOCK
        """
        if search_flag == "ALL":
            sql = f"SELECT product_name, cost, price, stock, location, reorder_level FROM {self.table_name}"
        elif search_flag == "IN_STOCK":
            sql = (f"SELECT product_name, cost, price, stock, location, reorder_level FROM {self.table_name} "
                   f"WHERE stock>0")
        elif search_flag == "NO_STOCK":
            sql = (f"SELECT product_name, cost, price, stock, location, reorder_level FROM {self.table_name} "
                   f"WHERE stock<=0")
        elif search_flag == "RE_ORDER":
            sql = (f"SELECT product_name, cost, price, stock, location, reorder_level FROM {self.table_name} "
                   f"WHERE stock<=reorder_level")
        else:
            sql = (f"SELECT product_name, cost, price, stock, location, reorder_level FROM {self.table_name} "
                   f"WHERE product_name='{product_name}'")

        # Execute the SQL statement
        result = self.common_search_all_execute(sql=sql)
        return result

    def delete_product(self, product_name):
        # Delete a product from the table
        sql = f"DELETE from {self.table_name} WHERE product_name='{product_name}'"
        result = self.common_update_execute(sql=sql)
        return result

    def get_product_names(self, product_name):
        # Retrieve product names based on a partial or complete name
        sql = f"SELECT product_name FROM {self.table_name} WHERE product_name LIKE '%{product_name}%'"
        search_result = self.common_search_all_execute(sql=sql)
        return search_result

    def get_single_product_info(self, product_name):
        # Retrieve information about a single product
        sql = f"SELECT stock, reorder_level, location FROM {self.table_name} WHERE product_name='{product_name}'"
        search_result = self.common_search_one_execute(sql=sql)
        return search_result

    def get_current_stock(self):
        # Retrieve the sum of all stocks in the table
        sql = f"SELECT sum(stock) FROM {self.table_name}"
        search_result = self.common_search_one_execute(sql=sql)
        return search_result

    def get_stock_value(self):
        # Retrieve the sum of the value of all stocks in the table
        sql = f"SELECT sum(price*stock) FROM {self.table_name}"
        search_result = self.common_search_one_execute(sql=sql)
        return search_result

    def get_stock_cost(self):
        # Retrieve the sum of the cost of all stocks in the table
        sql = f"SELECT sum(cost*stock) FROM {self.table_name}"
        search_result = self.common_search_one_execute(sql=sql)
        return search_result

    def get_reorder_product(self):
        # Retrieve the count of products that need to be reordered
        sql = f"SELECT count(*) FROM {self.table_name} WHERE reorder_level>=stock "
        search_result = self.common_search_one_execute(sql=sql)
        return search_result

    def get_no_stock_product(self):
        # Retrieve the count of products with no stock
        sql = f"SELECT count(*) FROM {self.table_name} WHERE stock<=0 "
        search_result = self.common_search_one_execute(sql=sql)
        return search_result

    def update_stock(self, **kwargs):
        # Update the stock of a product
        sql = f""" UPDATE {self.table_name} SET 
                    stock={kwargs["stock"]}
                   WHERE product_name='{kwargs["product_name"]}';
                """

        # Execute the SQL statement
        result = self.common_update_execute(sql)
        return result
