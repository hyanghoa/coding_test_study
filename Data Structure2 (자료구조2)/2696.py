import sys
import bisect

            
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    if n < 10:
        nums = sys.stdin.readline().split()
    else:
        nums = []
        for _ in range(n//10+1):
            nums.extend(sys.stdin.readline().split())
    answer = []
    tmp = []
    for idx, num in enumerate(nums, start=1):
        bisect.insort(tmp, int(num))
        if idx % 2 != 0:
            answer.append(tmp[idx//2])
    print(len(answer))
    print(*answer)