import sys
import heapq


hq = []
for i in range(int(input())):
    x = int(sys.stdin.readline().rstrip())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)