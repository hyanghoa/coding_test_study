import sys


answer = []
for _ in range(int(input())):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        answer.append(command[1])
    elif command[0] == "pop":
        if answer:
            print(answer.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(answer))
    elif command[0] == "empty":
        if answer:
            print(0)
        else:
            print(1)
    elif command[0] == "top":
        if answer:
            print(answer[-1])
        else:
            print(-1)