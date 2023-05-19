import sys
import heapq


for _ in range(int(input())):
    hq_min = []
    hq_max = []
    answer = {}
    for _ in range(int(input())):
        d, n = sys.stdin.readline().split()
        n = int(n)
        if d == "I":
            heapq.heappush(hq_min, n)
            heapq.heappush(hq_max, (-n, n))
            if answer.get(n) is not None:
                answer[n] += 1
            else:
                answer[n] = 1
        elif d == "D":
            if n == 1 and hq_max:
                while hq_max:
                    h = heapq.heappop(hq_max)[1]
                    if answer.get(h) is not None:
                        if answer[h] > 1:
                            answer[h] -= 1
                        else:
                            answer.pop(h)
                        break
            elif n == -1 and hq_min:
                while hq_min:
                    h = heapq.heappop(hq_min)
                    if answer.get(h) is not None:
                        if answer[h] > 1:
                            answer[h] -= 1
                        else:
                            answer.pop(h)
                        break
            if not hq_max or not hq_min:
                hq_max = []
                hq_min = []
                
    if answer:
        print(max(answer), min(answer))
    else:
        print("EMPTY")