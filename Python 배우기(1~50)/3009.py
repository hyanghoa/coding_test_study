coord = {"x": {}, "y": {}}
for _ in range(3):
    x, y = map(int, input().split())
    if coord["x"].get(x):
        coord["x"][x] += 1
    else:
        coord["x"][x] = 1
    if coord["y"].get(y):
        coord["y"][y] += 1
    else:
        coord["y"][y] = 1
        
x = sorted(coord["x"].items(), key=lambda x: x[1])[0][0]
y = sorted(coord["y"].items(), key=lambda x: x[1])[0][0]
print(x, y)