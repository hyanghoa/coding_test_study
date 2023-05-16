from collections import deque


t = int(input())
nums = deque([(int(n), idx+1) for idx, n in enumerate(input().split())])
answer = []
for _ in range(t):
    cur = nums.popleft()
    if cur[0] > 0:
        nums.rotate(-(cur[0]-1))
    else:
        nums.rotate(-(cur[0]))
    answer.append(cur[1])
print(*answer)