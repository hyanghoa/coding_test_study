import sys
import heapq


hq = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (-n, n))