
class ReadUserData:
    @staticmethod
    def user_to_dict(user):
        return {
            "user": {
                'userId': user.userId,
                'firstName': user.firstName,
                'lastName': user.lastName
            }
        }
