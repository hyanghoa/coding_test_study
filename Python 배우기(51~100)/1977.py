m = int(input())
n = int(input())
result_list = []
for i in range(min(m, n), max(m, n)+1):
    if len(str(i**0.5).split(".")[-1]) == 1:
        result_list.append(i)

if result_list:
    print(sum(result_list))
    print(result_list[0])
else:
    print(-1)