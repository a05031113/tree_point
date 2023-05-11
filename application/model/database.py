from dotenv import load_dotenv
import mysql.connector as connector
import os
load_dotenv()


class rds:
    def __init__(self):
        self.db = connector.connect(
            pool_name="mypool",
            pool_size=5,
            host=os.getenv("RDS_host"),
            user="root",
            password=os.getenv("sql_password"),
            database="point"
        )

    def check_user(self, username):
        cursor = self.db.cursor(buffered=True, dictionary=True)
        search = ("""
            SELECT id FROM users
            WHERE username = %s
            """)
        value = (username,)
        cursor.execute(search, value)
        output = cursor.fetchall()
        cursor.close()
        self.db.close()
        return output

    def add_user(self, username):
        cursor = self.db.cursor()
        insert = """
            INSERT INTO users
            (username) VALUES (%s)
            """
        value = (username,)
        cursor.execute(insert, value)
        self.db.commit()
        cursor.close()
        self.db.close()
        return True

    def received_or_used_point(self, user_id, point):
        cursor = self.db.cursor()
        insert = """
            INSERT INTO points
            (user_id, received_used) VALUES (%s, %s)
            """
        value = (user_id, point)
        cursor.execute(insert, value)
        self.db.commit()
        cursor.close()
        self.db.close()
        return True

    def total_point(self, username):
        cursor = self.db.cursor(buffered=True, dictionary=True)
        search = ("""
            SELECT users.id, SUM(received_used) as total_points
            FROM points 
            INNER JOIN users ON users.id = points.user_id
            WHERE username = %s
            """)
        value = (username,)
        cursor.execute(search, value)
        output = cursor.fetchall()
        cursor.close()
        self.db.close()
        return output
