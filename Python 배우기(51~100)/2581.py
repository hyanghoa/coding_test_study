def get_primes(m, n):
    check = [False, False] + [True] * (n-1)
    primes = []
    for i in range(2, n+1):
        if check[i]:
            if i >= m:
                primes.append(i)
            for j in range(i*2, n+1, i):
                check[j] = False
    return primes

m = int(input())
n = int(input())
primes = get_primes(m, n)
if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)