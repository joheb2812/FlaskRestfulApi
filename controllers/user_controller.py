from flask_restful import Resource
from models.user_model import UserModel
from models.user_model_old import UserModelOld
from utilities.database_sqlalchmy import db

class GetUserData(Resource):
    @staticmethod
    def get(user_id):
        model = UserModel(db)
        user_data = model.get_user_data(user_id)
        return user_data


class GetAllUsers(Resource):
    @staticmethod
    def get():
        model = UserModel(db)
        print("user model = %s", model)
        users_data = model.get_all_users()
        return users_data


# class GetAllUsersOld(Resource):
#     @staticmethod
#     def get():
#         model = UserModelOld()
#         users_data = model.get_all_users_old()
#         return users_data
#
#
# class GetUserDataOld(Resource):
#     @staticmethod
#     def get(user_id):
#         model = UserModelOld()
#         users_data = model.get_user_data_old(user_id)
#         return users_data
