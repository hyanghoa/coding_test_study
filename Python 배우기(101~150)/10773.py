import sys


n_list = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0:
        n_list.pop()
    else:
        n_list.append(n)
print(sum(n_list))