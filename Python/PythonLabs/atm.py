import sys

class bankAccount:
    def __init__(self, accountNo, title, firstName, lastName, balance):
        self.accountNo = accountNo
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount

def main():
    accounts = []
    #accounts.append("1057,Mr.,Jeremy,Clarkson,172.16")
    #accounts.append("2736,Miss.,Suzanne,Perry,15.62")
    #accounts.append("4069,Mrs.,Vicki,Butler-Henderson,23.91")
    #accounts.append("5691,Mr.,Jason,Plato,62.17")
    #print(accounts[1])
    
    lines = open("account.txt").readlines()
    for line in lines:
        accounts.append(bankAccount(*line.split(',')))
    
    for account in accounts:
        print(account.accountNo + ' ' + account.firstName + ' ' + account.lastName)

    invalid = True
    while invalid:
        choice = int(input("Enter account ID: "))
        if choice == 99999:
            print("\nATM Shutting down, Goodbye\n")
            sys.exit()
        elif len(str(choice)) == 4:
            print(account.accountNo[0])
            print(account.accountNo[1])
            print(account.accountNo[2])
            print(account.accountNo[3])


main()