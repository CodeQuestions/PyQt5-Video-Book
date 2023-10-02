import mysql.connector


class ConnectDatabase:
    def __init__(self):
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "testuser"
        self._password = "codequestions"
        self._database = "db_students"
        self.con = None
        self.cursor = None

    def connect_db(self):
        # Establish a database connection
        self.con = mysql.connector.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password
        )

        # Create a cursor for executing SQL queries
        self.cursor = self.con.cursor(dictionary=True)

    def add_info(self, student_id, first_name, last_name, state, city, email_address):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for adding information
        sql = f"""
            INSERT INTO students_info (studentId, firstName, lastName, state, city, emailAddress) 
	            VALUES ({student_id}, '{first_name}', '{last_name}', '{state}', '{city}', '{email_address}');
        """

        try:
            # Execute the SQL query for adding information
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()

    def update_info(self, student_id, first_name, last_name, state, city, email_address):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for updating information
        sql = f"""
            UPDATE students_info
                SET firstName='{first_name}', lastName='{last_name}', state='{state}', city='{city}', 
                    emailAddress='{email_address}'
                WHERE studentId={student_id};
        """

        try:
            # Execute the SQL query for updating information
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()

    def delete_info(self, studentId):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for deleting information
        sql = f"""  
            DELETE FROM students_info WHERE studentId={studentId};
        """

        try:
            # Execute the SQL query for deleting information
            self.cursor.execute(sql)
            self.con.commit()

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()

    def search_info(self, student_id=None, first_name=None, last_name=None, state=None, city=None, email_address=None):
        # Connect to the database
        self.connect_db()

        condition = ""
        if student_id:
            condition += f"studentId LIKE '%{student_id}%'"
        else:
            if first_name:
                if condition:
                    condition += f" and firstName LIKE '%{first_name}%'"
                else:
                    condition += f"firstName LIKE '%{first_name}%'"

            if last_name:
                if condition:
                    condition += f" and lastName LIKE '%{last_name}%'"
                else:
                    condition += f"lastName LIKE '%{last_name}%'"

            if state:
                if condition:
                    condition += f" and state='{state}'"
                else:
                    condition += f"state='{state}'"

            if city:
                if condition:
                    condition += f" and city='{city}'"
                else:
                    condition += f"city='{city}'"

            if email_address:
                if condition:
                    condition += f" and emailAddress LIKE '%{email_address}%'"
                else:
                    condition += f"emailAddress LIKE '%{email_address}%'"

        if condition:
            # Construct SQL query for searching information with conditions
            sql = f"""
                SELECT * FROM students_info WHERE {condition};
            """
        else:
            # Construct SQL query for searching all information
            sql = f"""
                SELECT * FROM students_info;
             """

        try:
            # Execute the SQL query for searching information
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as E:
            return E

        finally:
            # Close the database connection
            self.con.close()

    def get_all_states(self):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for deleting information
        sql = f"""  
            SELECT state FROM students_info GROUP BY state;
        """

        try:
            # Execute the SQL query for searching information
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()

    def get_all_cities(self):
        # Connect to the database
        self.connect_db()

        # Construct SQL query for deleting information
        sql = f"""  
            SELECT city FROM students_info GROUP BY city;
        """

        try:
            # Execute the SQL query for searching information
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result

        except Exception as E:
            # Rollback the transaction in case of an error
            self.con.rollback()
            return E

        finally:
            # Close the database connection
            self.con.close()
