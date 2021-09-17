#Usman Shoukat
#201537600
import datetime
import random
class BasicAccount:
    acNumIssuer = 0
    # initialization of attributes of BasicAccount Class
    def __init__(self, acName: str, openingBalance: float ):
        self.name: str = acName
        BasicAccount.acNumIssuer += 1
        self.acNum: int = BasicAccount.acNumIssuer
        self.balance: float = 0
        if openingBalance >=0:
            self.balance = openingBalance
        else:
            print("Opening balance for account number {self.acNum} is not valid. Enter right value and run program again.\n".format(self=self))
            exit()
        self.cardNum: str = ""
        self.cardExp: tuple(int,int) = ()
        self.issueNewCard()
    #__str__ method gives the brief description of instance
    def __str__(self):
        return "This is Basic Account of {self.name} with £{self.balance} balance available".format(self=self)
    #add the asked amount to balance of the instance
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print("{} have successfully deposited £{}. New balance is £{}".format(self.name,amount,self.balance))
        else:
            print("Sorry, entered amount is not valid ")
    #withdraws the asked amount from the balance of the instance
    def withdraw(self, amount: float):
        if amount > 0 and self.balance - amount >= 0:
            self.balance -= amount
            print("{} has withdrew £{}. New balance is £{}".format(self.name,amount,self.balance))
        else:
            print("Can not withdraw £{}".format(amount))
    #returns the avilable balance of the instance
    def getAvailableBalance(self) -> float:
        return self.balance
    #returns the balance of the account. If account is overdrawn, it returns a negative value.
    def getBalance(self) -> float:
        return self.balance
    #prints out the balance of the account
    def printBalance(self):
        print("The balance of account number {self.acNum} is £{self.balance}".format(self=self))
    #returns the name of account holder
    def getName(self) -> str:
        return self.name
    #returns the account number of account holder
    def getAcNum(self) -> str:
        return str (self.acNum)
    #Issues and update the credentials (card Nnumber, expiry date) of card of an instance
    def issueNewCard(self):
        self.cardNum = str(random.randint(1000000000000000,9999999999999999))
        today = datetime.datetime.now()
        self.cardExp = (today.month,(today.year + 3)%100)
    #returns the amount to user if account is not overdrawn and return True. If account is in debt, it return False.
    def closeAccount(self) -> bool:
        if self.balance >= 0:
            self.withdraw(self.balance)
            print("Your account is closed.")
            return True
        else:
            print("Can not close account due to customer being overdrawn by £{}".format(-self.balance))
            return False
#PremiumAccount is subclass of BasicAccount and is inheriting some of the methods from BasicAccount 
class PremiumAccount(BasicAccount):
    #Initializing of attributes
    def __init__(self, acName: str, openingBalance: float, initialOverdraft: float):
        #passing on attributes to superclass which are in common with superclass
        super().__init__(acName, openingBalance)
        self.overdraft : bool = False
        self.overdraftLimit: float = 0
        if initialOverdraft >= 0:
            self.overdraftLimit  = initialOverdraft
        else:
            print("Overdraft Limit for account number {self.acNum} is not valid. £0 is being set as overdraft Limit as for now. Use setOverdraftLimit method to set overdraft limit".format(self=self))
    #__str__ method gives the brief description of instance
    def __str__(self) -> str:
        if self.balance >= 0:
            return "This is Premium Account of {self.name} with £{self.balance} balance available. Your overdraft limit is £{self.overdraftLimit}.".format(self=self)
        else:
             return "This is Premium Account of {} with £{} balance withdrawn. Your overdraft limit is £{}.".format(self.name,-self.balance,self.overdraftLimit)
    #deposits the asked amount to the balance of user
    def deposit(self, amount: float):
        """
        deposit adds the asked amount to the bank balance of an account if the entered amount is valid
        and sets overdraft to False, if after adding amount, the account holder is not in debt anymore
        parameters:
            Account : The account in which the balance is to be added
            amount: Amount to be added
        Return:
            Nothing
        """
        if amount > 0:
            self.balance += amount
            print("{} have successfully deposited £{}. New balance is {}".format(self.name,amount,self.balance))
            if self.balance >= 0:
                self.overdraft = False
        else:
            print("Sorry, entered amount is not valid ")
    #withdraw the asked amount from the balance of user
    def withdraw(self, amount: float): 
        """
        withdraw subtracts the asked amount from the bank balance of an account if the entered amount is valid
        and sets overdraft to True, if after subtracting amount, the account holder goes in debt
        parameters:
            Account : The account from which the balance is to be withdrawn
            amount: Amount to be withdrawn
        Return:
            Nothing
        """ 
        if amount > 0 and (self.balance + self.overdraftLimit) - amount >= 0:
            self.balance -= amount
            if self.balance < 0:
                self.overdraft = True
            print("{} has withdrew £{}. New balance is £{}".format(self.name,amount,self.balance))
        else:
            print("Can not withdraw £{}".format(amount))
    #set the overdrat limt to asked value
    def setOverdraftLimit(self, newLimit: float):
        self.overdraftLimit = newLimit
    #returns collective balance (balance + overDraftAvailable)
    def getAvailableBalance(self) -> float:
        return self.balance + self.overdraftLimit
    #print out the balance of the user
    def printBalance(self):
        if self.balance >= 0:
            print("Your balance is £{} and you have £{} overdraft available".format(self.balance,self.overdraftLimit))
        else:
            print("You have overdrawn £{} and you have £{} overdraft available".format(-self.balance,self.balance+self.overdraftLimit))
    #It seemed redundant to me.
    #returns the amount to user if account is not overdrawn and return True. If account is in debt, it return False.
    def closeAccount(self) -> bool:
        if not self.overdraft:
            self.withdraw(self.balance)
            print("Your account is closed.\n")
            return True
        else:
            print("Can not close account due to customer being overdrawn by £{}".format(-self.balance))
            return False

def main():
    acc1 = BasicAccount("Alice",50)
    acc2 = PremiumAccount("John", 50,100)
    print(type(acc1))
    print(acc1.__dict__)
    print(type(acc2))
    print(acc2.__dict__)
if __name__ == "__main__":
    main()