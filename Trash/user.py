class Users:
    def __init__(self, Id, firstName, lastName):
        self.Id = Id
        self.firstName = firstName
        self.lastName = lastName

    def to_dict(self):
        return {
            "userId": self.Id,
            "firstName": self.firstName,
            "lastName": self.lastName
        }
