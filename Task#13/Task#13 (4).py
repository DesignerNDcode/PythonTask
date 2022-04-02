import random
Mates = ["Muhaimin", "Shoiab", "Yasir", "Nazzal", "Rehan", "Hammad"]
i = 1
score = []
while i <= 6:
    i = i+1
    random.seed(i)
    res = random.randrange(60, 90, 8)
    score.append(res)

for (m,s) in zip(Mates, score):
    print(m, "your score is", s)

