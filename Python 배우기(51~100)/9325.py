for _ in range(int(input())):
    s = int(input())
    total_price = s
    for _ in range(int(input())):
        q, p = map(int, input().split())
        total_price += q*p
    print(total_price)