import random
# Game #1 Data
g1 = ["Don't forget you are King", "you are Millionaire by heart", "You are cute", "you are dump",
      "You are kind hearted", "You are Sharp", "you are brave", "you are loving", "you are Handsome"]
# Game #2 Data
g2 = ["Red", "Orange", "Yellow", "Greem", "Blue", "Pink", "Purple", "Brown", "Black", "White"]
# Game #3 Data
g3 = ["alone", "You are the protector", "Kind hearted", "big dreamer", "Hard Worker"]

print("================Start================")
Ch = int(input(
    "Enter 1, for 'Who are you ?' 2, ' the color of your personality is?' 3,'know the meaning behind your name' ==="))
input("tell you name")
if Ch == 1:
    res = random.choice(g1)
    print(res)

elif Ch == 2:
    res = random.choice(g2)
    print(res)

elif Ch == 3:
    res = random.choice(g3)
    print(res)

else:
    print("wrong Option")
