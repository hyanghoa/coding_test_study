t = int(input())
for i in range(1, t+1):
    star = "*"*i
    print(star.rjust(t))
for i in reversed(range(1, t)):
    star = "*"*i
    print(star.rjust(t))