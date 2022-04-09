a = [['happy', 'BirtHday', 'to', 'yoU'], ['this', 'Is', 'MY', 'BdaY', 'Month'], ['wish', 'me', 'HappY', 'BirtHday'], ['i', 'did', 'it']]


for h in range(len(a)):
    for i in range(len(a[h])):
        a[h][i] = a[h][i].upper()
print(a)
