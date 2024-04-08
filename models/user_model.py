import logging
from utilities.database_sqlalchmy import Database
from flask_restful import abort
from utilities.database_class import User
from utilities.read_user_data import ReadUserData


class UserModel:
    def __init__(self, db: Database):
        self.db = db
        self.logger = logging.getLogger(__name__)

        # print("db = %s", self.db.engine.pool)
        # self.logger.log(logging.DEBUG, "db = %s", self.db)
        self.read_user_data = ReadUserData

    def get_user_data(self, user_id):
        session = None
        try:
            session = self.db.create_session()
            user = session.query(User).filter_by(userId=user_id).first()
            return self.read_user_data.user_to_dict(user)
        except Exception as e:
            self.logger.error(f"Error fetching user data: {e}")
            abort(404, message="User not found")
        finally:
            if session is not None:
                session.close()

    def get_all_users(self):
        session = None
        try:
            session = self.db.create_session()
            users = session.query(User).all()
            return [self.read_user_data.user_to_dict(user) for user in users]
        except Exception as e:
            self.logger.error(f"Error fetching user data: {e}")
            abort(500, message="Internal Server Error")
        finally:
            if session is not None:
                session.close()
