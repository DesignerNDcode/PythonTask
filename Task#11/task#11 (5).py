def atm():
    total_cash = 5000
    while True:
        choice = int(input("enter 1 for deposit 2 for withdraw 3 for check balance and 4 for exit"))
        if choice == 1:
            dep = int(input('Enter the amount ='))
            total_cash += dep
            print('Amount deposited successfully!')
            print('Your new balance is', total_cash)

        elif choice == 2:
            dep = int(input('Enter the amount ='))
            total_cash -= dep
            print('Amount deposited withdrawn!')
            print('Your new balance is', total_cash)

        elif choice == 3:
            print('Your total balance is', total_cash)

        elif choice == 4:
            break

        else:
            print("wrong option")


atm()
