n = int(input())
tower_list = list(map(int, input().split()))

stack = []
answer = [0] * n
index = 1
cur = tower_list.pop()
while tower_list:
    next_tower = tower_list.pop()
    if next_tower > cur:
        if stack:
            while stack:
                s = stack.pop()
                if s[0] < next_tower:
                    answer[s[1]] = n-index
                else:
                    stack.append(s)
                    break
        answer[n-index] = n-index
        cur = next_tower
    else:
        stack.append((cur, n-index))
        cur = next_tower
    index += 1
print(*answer)