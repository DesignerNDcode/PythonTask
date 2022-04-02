import random
dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
i = 0
while i <= 2:
    i = i+1
    print("YOu will get 3 chances")
    choice = input("Enter start to play game and exit to exit game =")
    if choice == "yes":
        result1 = random.choice(dice1)
        result2 = random.choice(dice2)
        print(result1, result2)

        if i == 3:
            if result1 != result2:
                print("==============You failed==============")

            else:
                print("==============you won==============")

    elif choice == "exit":
        break

    else:
        print("Wrong Choice")



