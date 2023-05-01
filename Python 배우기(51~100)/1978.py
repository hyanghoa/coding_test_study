def get_primes(n):
    check = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if check[i]:
            for j in range(i*2, n+1, i):
                check[j] = False
    return check

t = int(input())
n_list = list(map(int, input().split()))
primes = get_primes(1000)
answer = 0
for n in n_list:
    if primes[n]:
        answer += 1
print(answer)