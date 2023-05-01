n_list = list(filter(lambda x: x % 2 != 0, [int(input()) for _ in range(7)]))
if n_list:
    print(sum(n_list))
    print(min(n_list))
else:
    print(-1)