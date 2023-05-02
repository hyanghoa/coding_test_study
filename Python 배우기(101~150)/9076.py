t = int(input())
for _ in range(t):
    score_list = sorted(list(map(int, input().split())))[1:-1]
    if max(score_list) - min(score_list) >= 4:
        print("KIN")
    else:
        print(sum(score_list))