print("Welcome to python vending machine")
Demand = input("please let us know you want chocolates or cold drinks")
option1 = "cold drinks"
option2 = "chocolates"

st_fl = "pepsi", "fanta", "sprite", "deo"
ch_fl = "Dairy milk", "kitkat", "perk", "Coconut"

if Demand == "cold drinks":

    fl = input("Which flavour you want?")
    if fl in st_fl:
        print("enjoy your drink")
    else:
        print("flavour not available")


elif Demand == "chocolates":
    ch_fl = input("Which flavour you want?")
    if ch_fl in st_fl:
        print("Eat your chocolate")
    else:
        print("flavour not available")
else:
    print("invalid option")
