from utilities.database_connection_pool import Database
from flask_restful import abort
from Trash.user import Users
from Trash.transactions import Transaction
import logging



class UserModelOld:
    def __init__(self):
        self.db = Database()
        self.logger = logging.getLogger(__name__)

    def get_user_data_old(self, user_id):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE userId=%s", (user_id,))
            user_data = cursor.fetchone()
            if not user_data:
                cursor.close()
                abort(404, message="User not found")
            cursor.execute("SELECT * FROM transactions WHERE userId=%s ORDER BY transactionDate DESC LIMIT 5",
                           (user_data[0],))
            transaction_data = cursor.fetchall()
            transactions = []
            for data in transaction_data:
                transaction = Transaction(data[0],
                                          data[1].strftime("%Y-%m-%d"),
                                          float(data[2]),
                                          data[3]
                                          )
                transactions.append(transaction.__dict__)
            user = Users(user_data[0], user_data[1], user_data[2])
            return (
                {"user": user.__dict__,
                 "transactions": transactions})

        except MySQLdb.Error as e:
            self.logger.error(f"An error occurred: {e}")
            abort(500, message="Internal server error")
        finally:
            with conn.cursor() as cursor:
                cursor.close()
            conn.close()

    def get_all_users_old(self):
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.*, t.* 
                FROM users u 
                LEFT JOIN transactions t ON u.userId = t.userId 
                ORDER BY t.transactionDate DESC LIMIT 5
                """)
            users_data = cursor.fetchall()
            users = []
            transactions = []
            current_user = None
            for row in users_data:
                if current_user is None or current_user['userId'] != row[0]:
                    if current_user is not None:
                        users.append({"user": current_user, "transactions": transactions})
                    current_user = {
                        "userId": row[0],
                        "firstName": row[1],
                        "lastName": row[2]
                    }
                    transactions = []
                if row[3] is not None:
                    transaction = Transaction(
                        row[3],
                        row[4],
                        float(row[5]),
                        row[6]
                    )
                    transactions.append(transaction.to_dict())
            if current_user is not None:
                users.append({"user": current_user, "transactions": transactions})
            return users

        except MySQLdb.Error as e:
            self.logger.error(f"An error occurred: {e}")
            abort(500, message="Internal server error")
        finally:
            with conn.cursor() as cursor:
                cursor.close()
            conn.close()
