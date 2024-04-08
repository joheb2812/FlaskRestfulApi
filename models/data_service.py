import logging
from models.transaction_model import TransactionModel
from models.user_model import UserModel
from flask_restful import abort

from utilities.database_sqlalchmy import Database


class UserDataService:
    def __init__(self, db: Database):
        self.user_model = UserModel(db)
        self.transaction_model = TransactionModel(db)
        self.logger = logging.getLogger(__name__)

    def get_users_with_transactions(self):
        users_with_transactions = []
        try:
            all_users = self.user_model.get_all_users()
            for user_data in all_users:
                user_id = user_data["user"]["userId"]
                transactions = self.transaction_model.get_transactions_by_user_id(user_id)
                user_with_transactions = {
                    "user": user_data["user"],
                    "transactions": transactions
                }
                users_with_transactions.append(user_with_transactions)
            return users_with_transactions
        except Exception as e:
            self.logger.error(f"An error in users with transactions: {e}")
            abort(404, message="Data not found")
