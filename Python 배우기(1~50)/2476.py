def get_price(a, b, c):
    if a == b == c:
        return 10000+a*1000
    elif a == b != c:
        return 1000+a*100
    elif a != b == c:
        return 1000+b*100
    elif a == c != b:
        return 1000+a*100
    else:
        return max(a, b, c)*100
    
t = int(input())
price_list = []
for i in range(t):
    a, b, c = map(int, input().split())
    price = get_price(a, b, c)
    price_list.append(price)
print(max(price_list))