

class Transaction:
    def __init__(self, transactionId, transactionDate, amount, debitOrCredit):
        self.transactionId = transactionId
        self.transactionDate = transactionDate
        self.amount = amount
        self.debitOrCredit = debitOrCredit

    # def __str__(self):
    #     return self.transactionId

    def to_dict(self):
        return {
            "transactionId": self.transactionId,
            "transactionDate": self.transactionDate.strftime("%Y-%m-%d"),
            "amount": self.amount,
            "debitOrCredit": self.debitOrCredit
        }
