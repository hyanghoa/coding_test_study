score_list = []
for i in range(8):
    score = int(input())
    score_list.append((score, i))

print(sum([score for score, _ in sorted(score_list, reverse=True)[:5]]))
print(*sorted([index+1 for _, index in sorted(score_list, reverse=True)[:5]]))