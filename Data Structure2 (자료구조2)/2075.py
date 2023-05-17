import sys
import heapq


n = int(input())
n_list = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    n_list.extend(tmp)
    heapq.heapify(n_list)
    n_list = heapq.nlargest(n, n_list)
print(n_list[-1])