class Bank:

    def __init__(self, accountName, accountNo, accountIBAN, accountBalance, accountPIN, accountStatement=[]):
        self.accountName = accountName
        self.accountNo = accountNo
        self.accountIBAN = accountIBAN
        self.accountBalance = accountBalance
        self.accountPIN = accountPIN




        #getters

        def getBalance(self):
            return "{}".format(self.accountBalance)

        #setters

        def lodgeAccount(self, amount):
            self.accountBalance += amount

        def viewStatement(self):








