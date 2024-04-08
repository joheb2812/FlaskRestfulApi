import mysql.connector.pooling
from dotenv import load_dotenv
import os

load_dotenv()


class Database:
    pool = None

    @classmethod
    def get_connection_pool(cls):
        if cls.pool is None:
            cls.pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="mypool",
                pool_size=5,
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD'),
                database=os.getenv('MYSQL_DB')
            )
        return cls.pool

    @classmethod
    def get_connection(cls):
        try:
            return cls.get_connection_pool().get_connection()
        except mysql.connector.Error as e:
            print(f"An error occurred while establishing connection {e}")
