for _ in range(int(input())):
    n_list = list(map(int, input().split()))
    n_list = [n for n in n_list if n % 2 == 0]
    print(sum(n_list), min(n_list))