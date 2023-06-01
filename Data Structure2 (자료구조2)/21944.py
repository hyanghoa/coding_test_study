import sys
import heapq
from collections import defaultdict


class Solution:
    def __init__(self):
        self.workbook_info = {}
        self.min_algorithm = defaultdict(list)
        self.max_algorithm = defaultdict(list)
        self.min_level = defaultdict(list)
        self.max_level = defaultdict(list)

    def recommend(self, g, x):
        g, x = int(g), int(x)
        algorithm = self.max_algorithm[g] if x == 1 else self.min_algorithm[g]
        while algorithm:
            recommend_l, recommend_p = abs(algorithm[0][0]), abs(algorithm[0][1])
            if self.workbook_info.get(recommend_p) is not None and self.workbook_info[recommend_p][0] == recommend_l and self.workbook_info[recommend_p][1] == g:
                print(recommend_p)
                break
            else:
                heapq.heappop(algorithm)

    def recommend2(self, x):
        x = int(x)
        if x == 1:
            while self.max_level:
                max_level = max(self.max_level)
                while self.max_level[max_level]:
                    p, g = -self.max_level[max_level][0][0], -self.max_level[max_level][0][1]
                    if self.workbook_info.get(p) is not None and self.workbook_info[p][0] == max_level and self.workbook_info[p][1] == g:
                        print(p)
                        return
                    else:
                        heapq.heappop(self.max_level[max_level])
                self.max_level.pop(max_level)
        elif x == -1:
            while self.min_level:
                min_level = min(self.min_level)
                while self.min_level[min_level]:
                    p, g = self.min_level[min_level][0][0], self.min_level[min_level][0][1]
                    if self.workbook_info.get(p) is not None and self.workbook_info[p][0] == min_level and self.workbook_info[p][1] == g:
                        print(p)
                        return
                    else:
                        heapq.heappop(self.min_level[min_level])
                self.min_level.pop(min_level)

    def recommend3(self, x, l):
        x, l = int(x), int(l)
        if x == 1:
            while self.min_level:
                min_level = 101
                for ml in self.min_level:
                    if l <= ml:
                        min_level = min(min_level, ml)
                while self.min_level[min_level]:
                    p, g = self.min_level[min_level][0][0], self.min_level[min_level][0][1]
                    if self.workbook_info.get(p) is not None and self.workbook_info[p][0] == min_level and self.workbook_info[p][1] == g:
                        print(p)
                        return
                    else:
                        heapq.heappop(self.min_level[min_level])
                if min_level == 101:
                    print(-1)
                    return
                else:
                    self.min_level.pop(min_level)
        elif x == -1:
            while self.max_level:
                max_level = 0
                for ml in self.max_level:
                    if l > ml:
                        max_level = max(max_level, ml)
                while self.max_level[max_level]:
                    p, g = -self.max_level[max_level][0][0], -self.max_level[max_level][0][1]
                    if self.workbook_info.get(p) is not None and self.workbook_info[p][0] == max_level and self.workbook_info[p][1] == g:
                        print(p)
                        return
                    else:
                        heapq.heappop(self.max_level[max_level])
                if max_level == 0:
                    print(-1)
                    return
                else:
                    self.max_level.pop(max_level)

    def add(self, p, l, g):
        p, l, g = int(p), int(l), int(g)
        self.workbook_info[p] = (l, g)
        heapq.heappush(self.min_algorithm[g], (l, p))
        heapq.heappush(self.max_algorithm[g], (-l, -p))
        heapq.heappush(self.min_level[l], (p, g))
        heapq.heappush(self.max_level[l], (-p, -g))

    def solved(self, p):
        p = int(p)
        self.workbook_info.pop(p)
    

s = Solution()
for _ in range(int(input())):
    p, l, g = map(int, sys.stdin.readline().split())
    s.add(p, l, g)

for _ in range(int(input())):
    c = sys.stdin.readline().split()
    if c[0] == "recommend":
        s.recommend(c[1], c[2])
    elif c[0] == "recommend2":
        s.recommend2(c[1])
    elif c[0] == "recommend3":
        s.recommend3(c[1], c[2])
    elif c[0] == "add":
        s.add(c[1], c[2], c[3])
    elif c[0] == "solved":
        s.solved(c[1])