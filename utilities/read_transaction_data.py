
class ReadTransactionData:
    @staticmethod
    def transaction_to_dict(transaction):
        return {
                'transactionId': transaction.transactionId,
                'transactionDate': transaction.transactionDate.strftime("%Y-%m-%d"),
                'amount': transaction.amount,
                "debitOrCredit": transaction.debitOrCredit
            }

