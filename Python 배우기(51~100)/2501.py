def get_divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor

n, k = map(int, input().split())
divisor = get_divisor(n)
if len(divisor) < k:
    print(0)
else:
    print(divisor[k-1])