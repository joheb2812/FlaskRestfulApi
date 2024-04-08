from flask import Flask
from flask_restful import Api
from controllers.user_controller import *
from controllers.transaction_controller import *

app = Flask(__name__)
api = Api(app)


api.add_resource(GetUserData, "/user/<int:user_id>")
api.add_resource(GetAllUsers, "/users")
api.add_resource(GetAllTransactions, "/transactions")
api.add_resource(GetAllTransactionsAllUsers, "/users/transactions")
# api.add_resource(GetAllUsersOld, "/users/old")
# api.add_resource(GetUserDataOld, "/user/old/<int:user_id>")
if __name__ == '__main__':
    app.run(debug=True)
