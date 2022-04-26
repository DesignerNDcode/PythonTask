class BankAccount:
    name = 'Muhaimin'
    accountNumber = 476854781
    balance = 5000

    def __init__(self, accountNumber, name, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, deposit):
        self.balance = deposit + self.balance

    def withdraw(self, wd):
        self.balance = self.balance - wd

    def bankfees(self, fees):
        fees_calc = self.balance / 100 * fees
        self.balance = self.balance - fees_calc

    def display(self):
        print("Account No. :", self.accountNumber,
              "\n", "Name :", self.name,
              "\n", self.balance)


# object
Data = BankAccount(4893541258, "yasir", 5000)
# object

# methods
Data.deposit(1000)
Data.withdraw(500)
Data.bankfees(5)

Data.display()
# methods

