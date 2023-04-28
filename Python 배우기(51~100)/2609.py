def get_gcd(a, b):
    while True:
        if a % b == 0:
            return b
        a, b = b, a % b

def get_lcm(a, b):
    return a*b//get_gcd(a, b)

a, b = map(int, input().split())
print(get_gcd(a, b))
print(get_lcm(a, b))