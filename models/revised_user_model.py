from utilities.database_sqlalchmy import Database
from flask_restful import abort
from utilities.database_class import User, Transaction


class UserModel:
    def __init__(self):
        self.db = Database()

    def get_user_data(self, userId):
        try:
            user = self.db.session.query(User).filter_by(userId=userId).first()
            transactions = self.db.session.query(Transaction).filter_by(userId=user.userId)
            transactions_data = [{'transactionId': t.transactionId,
                                  'transactionDate': t.transactionDate.strftime("%Y-%m-%d"),
                                  'amount': t.amount,
                                  'debitOrCredit': t.debitOrCredit} for t in transactions]

            return {
                "User": {'userId': user.userId,
                         'firstName': user.firstName,
                         'lastName': user.lastName},
                "transactions": transactions_data
            }

        except Exception as e:
            print(f"An error occurred while fetching user data: {e}")
            abort(404, message="User not found")

        finally:
            self.db.session.close()

    def get_all_users(self):
        try:
            users = self.db.session.query(User).all()
            users_data = []

            for data in users:
                transactions = self.db.session.query(Transaction).filter_by(userId=data.userId).order_by(
                    Transaction.transactionDate.desc()).limit(5).all()
                transactions_data = [{'transactionId': t.transactionId,
                                      'transactionDate': t.transactionDate.strftime("%Y-%m-%d"),
                                      'amount': t.amount,
                                      'debitOrCredit': t.debitOrCredit}
                                     for t in transactions]

                users_data.append({
                    "user": {'userId': data.userId,
                             'firstName': data.firstName,
                             'lastName': data.lastName},
                    'transactions': transactions_data
                })
            return users_data

        except Exception as e:
            print(f"An error occurred while fetching user data: {e}")
            abort(404, message="Data not found")

        finally:
            self.db.session.close()
