a = [['happy', 'BirtHday', 'to', 'yoU'], ['this', 'Is', 'MY', 'BdaY', 'Month'], ['wish', 'me', 'HappY', 'BirtHday']]

# List 1 of a
print("Before:", (a[0]))

for i in range(len(a[0])):
    a[0][i] = a[0][i].upper()

print("After:", (a[0]))

print("=======================")

# List 2 of a
print("Before:", (a[1]))

for i in range(len(a[1])):
    a[1][i] = a[1][i].upper()

print("After:", (a[1]))

print("=======================")

# List 3 of a
print("Before:", (a[2]))

for i in range(len(a[2])):
    a[2][i] = a[2][i].upper()

print("After:", (a[2]))
