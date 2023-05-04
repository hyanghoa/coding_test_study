from collections import deque


for _ in range(int(input())):
    n, m = map(int, input().split())
    nums = deque([(int(x), idx) for idx, x in enumerate(input().split())])
    answer = 1

    while True:
        cur = nums.popleft()
        if not nums:
            print(answer)
            break
        if cur[0] >= max(nums)[0]:
            if cur[1] == m:
                print(answer)
                break
            answer += 1
        else:
            nums.append(cur)