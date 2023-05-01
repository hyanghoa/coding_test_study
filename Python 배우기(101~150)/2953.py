score_list = []
for i in range(1, 6):
    score = sum(list(map(int, input().split())))
    score_list.append((score, i))

answer = sorted(score_list)[-1]
print(answer[1], answer[0])