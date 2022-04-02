# linear will solve bx = b or ax = b
def linear_Equation(a, b):
    if a == b:
        print(a + b )
    elif a > 0:
        x = -b / a

        print('The value of x is:', x)
    else:
        print('invalid input')


linear_Equation(5, 5)
