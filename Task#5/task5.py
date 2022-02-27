# -----------Task1-----------
print('-----------Task1-----------')
print('Hello Welcome to CalcPY')
a = int(input('Enter first digit'))
b = int(input('Enter seccond digit'))
print(a + b, "Added")
print(a - b, "substracted")
print(a / b, "Divided")
print(a * b, "multiplied")
print(a // b, "floor divided")

# -----------Task2-----------
print('-----------Task2-----------')
first = int(input('Enter first argument'))
seccond = int(input('Enter seccond argument'))
print(first == seccond)

# -----------Task3-----------
print('-----------Task3-----------')
print('Welcome to Area Calculator')
width = float(input("enter the width"))
length = float(input("enter the length"))
print("Your plot total are is", width * length)

# -----------Task4-----------
print('-----------Task4-----------')
print("BMI calc in metrics ")
weight = float(input("enter weight in kilograms"))
height = float(input("enter height in cm"))

print(weight / (height / 100) ** 2, "Answer in metric")

print("BMI calc in US------- ")

print("BMI calc in us ")
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))
print('Your body mass index is: ', (weight / (height ** 2)) * 703)

# -----------Task5-----------
print('-----------Task5-----------')
print('Welcome to Converting Calculator')
# User weight in kG into pounds
weight = float(input("Enter your weight in kg"))
print("your weight in pounds is", weight * 2.2)

print('-----------AREA OF TRAPEZOID-----------')
b1 = int(input('Enter the length of base 1: '))
b2 = int(input('Enter the length of base 2: '))
height1 = int(input('Enter the height of trapezoid: '))
print('The area of the given trapezoid = ', ((b1 + b2) / 2) * height1)

print('-----------AREA OF PARRALLELOGRAM-----------')
base = int(input('Enter the length of base: '))
height = int(input('Enter the height of parrallelogram: '))
print('The area of the given parrallelogram = ', base * height)

print('-----------AREA  AND VOLUME OF CYLINDER-----------')

radius = int(input('Enter the radius of cylinder: '))
hc = int(input('Enter the height of the cylinder: '))
print('Surface area of cylinder = ', 2 * 3.14 * (radius + hc))
print('Volume of cylinder = ', 3.14 * (radius ** 2) * hc)
