import sys
import heapq


class Solution:
    def __init__(self):
        self.work_book = {}
        self.max_heap = []
        self.min_heap = []

    def recommend(self, x):
        x = int(x)
        if x == 1:
            while self.max_heap:
                p = -self.max_heap[0][1]
                l = -self.max_heap[0][0]
                count = self.work_book[p][1]
                level = self.work_book[p][0]
                if level == l and count > 0:
                    print(-self.max_heap[0][1])
                    break
                else:
                    heapq.heappop(self.max_heap)
        elif x == -1:
            while self.min_heap:
                p = self.min_heap[0][1]
                l = self.min_heap[0][0]
                count = self.work_book[p][1]
                level = self.work_book[p][0]
                if level == l and count > 0:
                    print(self.min_heap[0][1])
                    break
                else:
                    heapq.heappop(self.min_heap)
    
    def add(self, p, l):
        p, l = int(p), int(l)
        self.work_book[p] = (l, 1)
        heapq.heappush(self.min_heap, (l, p))
        heapq.heappush(self.max_heap, (-l, -p))

    def solved(self, p):
        p = int(p)
        self.work_book[p] = (self.work_book[p], 0)
    

solution = Solution()
for _ in range(int(input())):
    p, l = sys.stdin.readline().split()
    solution.add(p, l)
    
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == "recommend":
        solution.recommend(command[1])
    elif command[0] == "add":
        solution.add(command[1], command[2])
    elif command[0] == "solved":
        solution.solved(command[1])