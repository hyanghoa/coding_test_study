t = input()
total_score = 0
score_weight = 1
for i in map(int, input().split()):
    if i == 1:
        total_score += score_weight
        score_weight += 1
    else:
        score_weight = 1
print(total_score)