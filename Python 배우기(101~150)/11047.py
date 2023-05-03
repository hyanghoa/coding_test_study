n, k = map(int, input().split())
coin_list = sorted([int(input()) for _ in range(n)], reverse=True)
answer = 0
for coin in coin_list:
    answer += k // coin
    k %= coin
    if k == 0: break
print(answer)