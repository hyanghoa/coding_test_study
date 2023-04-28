t = int(input())
for i in reversed(range(0, t*2, 2)):
    space = " "*i
    print(space.center(t*2, "*"))
for i in range(2, t*2, 2):
    space = " "*i
    print(space.center(t*2, "*"))