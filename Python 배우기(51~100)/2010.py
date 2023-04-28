import sys


t = int(input())
total = 0
for _ in range(t):
    total += int(sys.stdin.readline())
print(total-t+1)