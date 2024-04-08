from flask_restful import Resource
from models.transaction_model import TransactionModel
from models.data_service import UserDataService
from utilities.database_sqlalchmy import db

class GetAllTransactions(Resource):
    @staticmethod
    def get():
        model = TransactionModel(db)
        transaction_data = model.get_all_transactions()
        return transaction_data


class GetAllTransactionsAllUsers(Resource):
    @staticmethod
    def get():
        model = UserDataService(db)
        transaction_data = model.get_users_with_transactions()
        return transaction_data
