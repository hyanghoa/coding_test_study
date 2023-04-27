n = int(input())
for _ in range(n):
    p = int(input())
    price_dict = {}
    
    for _ in range(p):
        c, name = input().split()
        price_dict[name] = int(c)
    
    print(sorted(price_dict.items(), key=lambda x: x[1], reverse=True)[0][0])