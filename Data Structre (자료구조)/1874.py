import sys


t = int(input())
nums = [int(sys.stdin.readline().strip()) for _ in range(t)]
stack = []
answer = []
cur = 0
for i in range(1, t+1):
    stack.append(i)
    answer.append("+")
    if nums[cur] <= stack[-1]:
        while stack:
            if nums[cur] > stack[-1]:
                break
            answer.append("-")
            if nums[cur] == stack.pop():
                cur += 1
if cur != len(nums):
    print("NO")
else:
    for ans in answer:
        print(ans)