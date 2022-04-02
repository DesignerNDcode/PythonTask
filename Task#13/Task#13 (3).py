import random
int = []

i = 1
while i <= 100:
    i = i+1
    skill = random.randrange(1, 100, 1)
    int.append(skill)


print(int)
for i in int:
    res = int.count(i)
    print(i, "Comes", res, "times")
