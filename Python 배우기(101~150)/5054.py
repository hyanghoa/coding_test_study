for _ in range(int(input())):
    location = int(input())
    n_list = sorted(list(map(int, input().split())))
    diff_list = []
    for a, b in zip(n_list, n_list[1:]):
        diff_list.append(abs(a-b))
    print(sum(diff_list)*2)