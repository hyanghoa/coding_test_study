from itertools import combinations


n_list = [int(input()) for _ in range(9)]
for c in combinations(n_list, 7):
    if sum(c) == 100:
        for x in sorted(c):
            print(x)
        break