import sys
import heapq
from collections import defaultdict


class Solution:
    def __init__(self):
        self.workbook_info = {}
        self.algorithm = defaultdict({"min": list, "max": list})
        self.level = defaultdict({"min": list, "max": list})

    def recommend(self, g, x):
        g, x = int(g), int(x)
        algorithm = self.max_algorithm[g] if x == 1 else self.min_algorithm[g]
        while algorithm:
            recommend_l, recommend_p = abs(algorithm[0][0]), abs(algorithm[0][1])
            info = self.workbook_info.get(recommend_p)
            if info is not None and info[0] == recommend_l and info[1] == g:
                print(recommend_p)
                break
            else:
                heapq.heappop(algorithm)

    def recommend2(self, x):
        x = int(x)
        key = "max" if x == 1 else "min"
        while self.level[key]:
            level = max(self.level[key]) if x == 1 else min(self.level[key])
            while self.level[key][level]:
                p, g = abs(self.level[key][level][0][0]), abs(self.level[key][level][0][1])
                info = self.workbook_info.get(p)
                if info is not None and info[0] == level and info[1] == g:
                    print(p)
                    return
                else:
                    heapq.heappop(self.level[key][level])
            self.level.pop(level)

    def recommend3(self, x, l):
        x, l = int(x), int(l)
        key = "max" if x == 1 else "min"
        while self.level[key]:
            level = 101 if x == 1 else 0
            for lv in self.level[key]:
                condition = l <= lv if x == 1 else l > lv
                if condition:
                    level = min(level, lv) if x == 1 else max(level, lv)
            while self.level[key][level]:
                p, g = abs(self.level[key][level][0][0]), abs(self.level[key][level][0][1])
                info = self.workbook_info.get(p)
                if info is not None and info[0] == level and info[1] == g:
                    print(p)
                    return
                else:
                    heapq.heappop(self.level[key][level])
            init_value = 101 if x == 1 else 0
            if level == init_value:
                print(-1)
                return
            else:
                self.level[key].pop(level)
        
    def add(self, p, l, g):
        p, l, g = int(p), int(l), int(g)
        self.workbook_info[p] = (l, g)
        heapq.heappush(self.algorithm[g]["min"], (l, p))
        heapq.heappush(self.algorithm[g]["max"], (-l, -p))
        heapq.heappush(self.level[l]["min"], (p, g))
        heapq.heappush(self.level[l]["max"], (-p, -g))

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