import sys


n, m = map(int, input().split())
name_dict = {}
number_dict = {}
for i in range(n+m):
    name = sys.stdin.readline().rstrip()
    if i >= n:
        if name.isdigit():
            print(number_dict[int(name)])
        else:
            print(name_dict[name])
    else:
        name_dict[name] = i+1
        number_dict[i+1] = name