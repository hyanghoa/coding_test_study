n = int(input())
result_dict = {}
for _ in range(n):
    name, d, m, y = input().split()
    result_dict[name] = (int(y), int(m), int(d))

result = sorted(result_dict.items(), key=lambda x: (x[1][0],x[1][1], x[1][2]) , reverse=True)
print(result[0][0])
print(result[-1][0])