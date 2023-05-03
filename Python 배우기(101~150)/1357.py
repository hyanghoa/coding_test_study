def rev(x):
    return int(str(x)[::-1])

x, y = input().split()
print(rev(rev(x)+rev(y)))