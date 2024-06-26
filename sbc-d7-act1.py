from random import randint

def bal(balance):
    use = input("Please Enter Your ID: ")
    if use == account:
          choice = (input("Would you like to proceed? y/n: "))
          if choice == "y":
            print(f"Hello your balance is {balance} php.")
          else:
              print("Operation Cancelled!")
    else:
        print('Invalid ID. Please try again.')
def deposit(balance):
    use = input("Please Enter Your ID: ")
    if use == account:
        amount = float(input("Please Enter your desired amount: "))
        choice = (input("Would you like to proceed? y/n: "))
        if choice == "y":
            if amount < 0:
                print("Enter a Valid Amount")
            else:
                balance += amount
                print(f"Deposit Successfully! Your new balance is {balance} php.")
                return balance
        else:
            print("Operation Cancelled!")
    else:
        print('Invalid ID. Please try again.')
        return balance()
def withdraw(balance):
    use = input("Please Enter Your ID: ")
    if use == account:
        amount = float(input("Please Enter your desired amount: "))
        choice = (input("Would you like to proceed? y/n: "))
        if choice == "y":
            if amount > balance:
                print("Insufficient Balance")
            elif amount < 0:
                print("Please Enter a Valid Amount")
            else:
                 balance -= amount
                 print(f"You withdraw sucessfully! Your new balance is {balance} php.")
        else:
            print("Operation Cancelled!")
    else:
        print('Invalid ID. Please try again.')
        return balance()
def delete():
    use = input("Please Enter Your ID: ")
    if use == account:
        choice = input("Are you sure you want to delete your account? y/n: ")
        if choice == "y":
            print("Account deleted successfully.")
            return True
        else:
            print("Operation canceled.")
    else:
        print("Invalid ID. Please try again.")
    return False

balance = 0 
bank = True
account = str(randint(00000, 99999))
data = {}

user = input("Enter Your Name: ")
data[account] = {"name": user, "balance": balance}
print(f"Hi {user}, this is your account ID {account}.")

while bank:
        use = input("Please Enter Your ID: ")
        if use == account:
            print("Welcome to XYZ Bank!")
        else:
            print("Enter a Valid Account ID")
        while bank:
            print("1 - Balance \n2 - Deposit \n3 - Withdraw \n4 - Delete Account")
            user = int(input("Enter a Choice: "))
            if user == 1:
                bal(data[account]["balance"])
            elif user == 2:
                data[account]["balance"] = deposit(data[account]["balance"])
            elif user == 3:
                data[account]["balance"] = withdraw(data[account]["balance"])
            elif user == 4:
                if delete():
                    bank = False
            else:
                print("Invalid Choice. Please try again.")
        else:
            print("Invalid ID. Please try again.")
