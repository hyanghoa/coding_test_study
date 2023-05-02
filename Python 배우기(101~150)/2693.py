for _ in range(int(input())):
    n_list = list(map(int, input().split()))
    print(sorted(n_list, reverse=True)[2])