import sys


n, m = map(int, input().split())
string_dict = {}
answer = 0
for i in range(n+m):
    string = sys.stdin.readline().rstrip()
    if i >= n:
        answer += string_dict.get(string, 0)
    else:
        string_dict[string] = 1
print(answer)