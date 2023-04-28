t = int(input())
for idx, i in enumerate(range(t*2-1, 0, -2)):
    star = "*"*i
    print(star.rjust(t*2-1-idx))
    
for idx, i in enumerate(range(3, t*2, 2)):
    star = "*"*i
    print(star.rjust(t+1+idx))