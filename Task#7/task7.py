print("------------------Task1 Start------------------")

current_balance = 5000
print("Welcome to PATM")
print("Choose one of the options below 1,2,3")
options = input("1. check balance 2. withdraw Amount 3. deposit amount ")

if int(options) == 1:
    print("you current balance is", current_balance)

elif int(options) == 2:
    amount_wt = int(input("Enter amount to withdraw"))
    if int(amount_wt) > current_balance:
        print('Insufficient balance')
    else:
        print('Amount withdrawn successfully!')

elif int(options) == 3:
    d_amount = int(input('Enter the amount you want to deposit'))
    current_balance += d_amount
    print('Amount Deposited successfully!')
    print('Your new balance is: ', current_balance)
else:
    print('Invalid choice')

print("------------------Task2 Start------------------")
req_Ex = 4
print("Welcome to Gamexone")
input("are you ready for interview?")
print("Okay")
name = input("What is Your name")
print("okay", name)

ex = int(input("How Much experience you have in this field?"))

if ex >= req_Ex:
    print("Thankyou, according to your experience you are nominated As programmer")

else:
    print("Thankyou, you are shortlisted as management person")

print("-----Task3-----")


hobby = input("enter your hobby")

if hobby == "arts" and 'drawing' and 'management':
    print("you can go for ARTS")

elif hobby == "bio" and "science" and "discipline":
    print("you can go for Medical")

elif hobby == 'logical' and 'programming' and 'problem solving' and 'technology':
    print("you can go for Engineering")

else:
    print("wrong info")


