import sys
from collections import deque


queue_list = deque()
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        queue_list.append(command[1])
    elif command[0] == "pop":
        if queue_list:
            print(queue_list.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue_list))
    elif command[0] == "empty":
        if queue_list:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if queue_list:
            print(queue_list[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue_list:
            print(queue_list[-1])
        else:
            print(-1)