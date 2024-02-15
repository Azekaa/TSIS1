class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, plus):
        self.balance += plus
        print(self.balance)
        
    def withdraw(self, minus):
        if minus > self.balance:
            print ("You cannot withdraw money, your balance is not enough to withdraw")
        else:
            self.balance -= minus
            print(self.balance)
    
    def exit(self):
        print ("POKA")
        
a = BankAccount(input("Your name: "), int(input("Your balance: ")))
n= input("operation(deposit , withdraw,exit):")
if n =="deposit":
    a.deposit(int(input("how much:")))
elif n == "withdraw":
    a.withdraw(int(input("how much:")))

else:
    print("error")