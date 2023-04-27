def get_gcd(a, b):
    for i in range(max(a, b), 0, -1):
        if a % i == 0 and b % i ==0:
            return i
    
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    gcd = get_gcd(a, b)
    lcm = a*b//gcd
    print(lcm)