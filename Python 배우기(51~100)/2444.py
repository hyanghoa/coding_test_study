t = int(input())
for idx, i in enumerate(range(1, t*2, 2)):
    star = "*"*i
    print(star.rjust(t+idx))
for idx, i in enumerate(reversed(range(1, t*2-1, 2))):
    star = "*"*i
    print(star.rjust(t+(t-idx-2)))