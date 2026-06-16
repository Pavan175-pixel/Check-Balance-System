def show_balance(balance):
    print ("my balance",balance)
    
def deposit():
    amount = float(input("Enter Amount:"))
    if amount<0:
        print("Invalid Amount")
        return 0
    else:
        return amount
        
def withdraw(balance):
    amount = float(input("Enter withdraw Amount:"))
    if amount>balance:
        print("Insufficient Balance")
        return 0
    elif amount<0:
        print("Invalid Amount")
        return 0
    else:
        return amount
        
def main():
    balance = 0
    condition = True
    while condition:
        print("1.show_balance, 2.deposit, 3.withdraw, 4.exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance = balance + deposit()
            print(balance)
        elif choice == 3:
            balance = balance - withdraw(balance)
        elif choice == 4:
            condition = False
        else:
            print("Invalid choice")
main()