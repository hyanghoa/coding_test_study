n = int(input())
star_list = ["*"]*n
star = " ".join(star_list)
for i in range(1, n+1):
    if i % 2 != 0:
        print(star)
    else:
        print(star.rjust(n*2))