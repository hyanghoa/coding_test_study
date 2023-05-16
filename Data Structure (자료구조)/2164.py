from collections import deque


n_list = deque(list(range(1, int(input())+1)))
while len(n_list) != 1:
    n_list.popleft()
    n_list.append(n_list.popleft())
print(n_list[0])