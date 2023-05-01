t = int(input())
scores = list(map(int, input().split()))
scores_new = list(map(lambda x: x/max(scores)*100, scores))
print(sum(scores_new)/t)