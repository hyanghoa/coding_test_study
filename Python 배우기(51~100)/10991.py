n = int(input())
for i in range(1, n+1):
    star = ["*"]*i
    star = " ".join(star)
    print(star.rjust(n-i+len(star)))