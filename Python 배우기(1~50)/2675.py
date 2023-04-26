t = int(input())
for _ in range(t):
    n, string = input().split()
    answer = ""
    for s in string:
        answer += s*int(n)
    print(answer)