
def isprime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            print(num, "is not prime Number")
            break
        else:
            print(num, "is prime number",  n)
isprime(8)
print("__________________")


# task Even
def iseven(num):
    if (num % 2) == 0:
        print(num, "is even number")
    else:
        print(num, "is not even number")

iseven(10)
print("__________________")
# task Even

# task odd

def isodd(num):
    if (num % 2) != 0:
        print(num, " is odd number")
    else:
        print(num, " is not odd number")

isodd(5)

# task odd

print("========== Task Mix ==========")
def num_check(num):
    if (num % 2) != 0:
        print(num, " is odd number")

    else:
        print(num, " is Even number")

    if num > 0:
        print(num, " is also positive number")

    else:
        print(num, "is also negati   ve number")

    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            print(num, "is not prime Number,")
            break
        else:
            print(num, "is also prime number",  n)

num_check(2)



