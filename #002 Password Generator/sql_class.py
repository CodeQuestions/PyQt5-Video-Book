from mysql import connector


class connectMySQL:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "test_user"
        self.password = "123456789"
        self.port = 3306
        self.database = "password_db"
        self.my_connector = None
        self.my_cursor = None

    def connect(self):
        """
        Connect to MySQL Database.
        """
        self.my_connector = connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )

        self.my_cursor = self.my_connector.cursor(dictionary=True, buffered=True)

    def get_data(self, sql):
        """
        Common function to get data from database.
        """
        self.connect()
        try:
            self.my_cursor.execute(sql)
            result = self.my_cursor.fetchall()

            return result

        except Exception as E:
            print(E)
            return

        finally:
            if self.my_connector:
                self.my_cursor.close()

    def update_data(self, sql):
        """
        Common function to update database.
        """
        self.connect()

        try:
            self.my_cursor.execute(sql)
            self.my_connector.commit()
        except Exception as E:
            self.my_connector.rollback()
            return E
        finally:
            if self.my_connector:
                self.my_cursor.close()

    ## function for login window
    def create_login_account(self, user_name, password):
        """
        Insert new login account data
        """
        sql = f"INSERT INTO user_tb (user_name, password) VALUES ('{user_name}', '{password}')"

        result = self.update_data(sql=sql)

        return result

    def check_username(self, username):
        """
        Check the username when create new login account.
        """
        sql = f"SELECT * FROM user_tb WHERE user_name='{username}'"

        result = self.get_data(sql=sql)

        return result

    ## Function for show data window
    def get_password_list(self, user_id, search_username, search_website):
        """
        Search and get password data from database.
        """
        sql = f"""
            SELECT * FROM password_tb 
                WHERE user_id={user_id} 
                    AND user_name LIKE '%{search_username}%'
                    AND website LIKE '%{search_website}%';
        """

        result = self.get_data(sql=sql)

        return result

    def delete_password_data(self, id):
        """
        Delete selected password data from database.
        """
        sql = f"DELETE FROM password_tb WHERE id={id}"

        result = self.update_data(sql=sql)

        return result

    ## Function for generate password window
    def save_new_password(self, user_id, user_name, website, password):
        """
        Save the new generate password data
        """
        sql = f"""
            INSERT INTO password_tb (user_id, user_name, website, password)
                VALUES ({user_id}, '{user_name}', '{website}', '{password}');
        """

        result =self.update_data(sql=sql)

        return result

    ## function for configuration window
    def create_config_data(self, user_id,
                           lowercase="abcdefghijklmnopqrstuvwxyz",
                           uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                           numbers="1234567890",
                           special_characters="@#$%&^!"):
        """
        Create configuration data for special account
        """
        sql = f"""
            INSERT INTO configuration_tb (user_id, lowercase, uppercase, numbers, special_characters )
	            VALUES ({user_id}, '{lowercase}', '{uppercase}', '{numbers}', '{special_characters}');
        """

        result = self.update_data(sql=sql)

        return result

    def check_config_data(self, user_id):
        """
        Check if the configuration data for the user is in the database.
        """
        sql = f"SELECT * FROM configuration_tb WHERE user_id={user_id}"

        result = self.get_data(sql=sql)

        return result

    def update_config_data(self, user_id, lowercase, uppercase, numbers, special_characters):
        """
        Update configuration data.
        """
        sql = f"""
            UPDATE configuration_tb 
                SET lowercase='{lowercase}', uppercase='{uppercase}',
                    numbers='{numbers}', special_characters='{special_characters}'
                WHERE user_id={user_id}
        """

        result = self.update_data(sql=sql)

        return result

















