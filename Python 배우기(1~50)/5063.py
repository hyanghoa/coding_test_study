n = int(input())
for _ in range(n):
    r, e, c = map(int, input().split())
    if e - r > c:
        print("advertise")
    elif e - r == c:
        print("does not matter")
    if e - r < c:
        print("do not advertise")