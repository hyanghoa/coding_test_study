t = int(input())

for _ in range(t):
    n = int(input())

    result = {}
    for _ in range(n):
        s, l = input().split()
        result[s] = int(l)
        
    answer = sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]
    print(answer)