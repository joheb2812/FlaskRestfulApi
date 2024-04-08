import logging
from flask_restful import abort
from utilities.database_class import Transaction
from utilities.database_sqlalchmy import Database
from utilities.read_transaction_data import ReadTransactionData


class TransactionModel:
    def __init__(self, db: Database):
        self.db = db
        self.read_transaction_data = ReadTransactionData
        self.logger = logging.getLogger(__name__)
        # self.logger.log(logging.DEBUG, "db = %s", self.db)

    def get_all_transactions(self):
        session = None
        try:
            session = self.db.create_session()
            transactions = session.query(Transaction).all()
            return [self.read_transaction_data.transaction_to_dict(transaction) for transaction in transactions]
        except Exception as e:
            self.logger.error(f"Failed to get all transactions: {e}")
            abort(404, message="Transaction data not found")
        finally:
            session.close()

    def get_transactions_by_user_id(self, user_id):
        session = None
        try:
            session = self.db.create_session()
            transactions = session.query(Transaction).filter_by(userId=user_id).all()
            return [self.read_transaction_data.transaction_to_dict(transaction) for transaction in transactions]
        except Exception as e:
            self.logger.error(f"Error while fetching transactions data: {e}")
            abort(404, message="Transaction data not found")

        finally:
            session.close()
