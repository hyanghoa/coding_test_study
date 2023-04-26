n = int(input())
x = 2
while x <= n:
    if n % x == 0:
        n /= x
        print(x)
    else:
        x += 1