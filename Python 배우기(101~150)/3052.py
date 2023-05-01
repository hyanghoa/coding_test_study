n_list = []
for _ in range(10):
    n = int(input()) % 42
    n_list.append(n)
print(len(list(set(n_list))))