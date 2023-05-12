import sys


n = int(input())
coord_list = []
stack = []
for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    coord_list.append((x-r, i))
    coord_list.append((x+r, i))
    
for coord in sorted(coord_list):
    if stack:
        if stack[-1][-1] == coord[1]:
            stack.pop()
        else:
            stack.append(coord)
    else:
        stack.append(coord)
    
if stack:
    print("NO")
else:
    print("YES")