# My concept is not cleared in this because I haven't Learned in school```
def quadratic(a, b, c):
    import cmath

    step = (b ** 2) - 4 * (a * c)
    step = cmath.sqrt(step)
    step = -b + step
    step = -b - step

    print('The 1st value of x is :', step)
    print('The second value of x is :', step)


quadratic(5, 5, 6)
