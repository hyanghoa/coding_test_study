for i in range(1, int(input())+1):
    print(f"Class {i}")
    n_list = sorted(list(map(int, input().split()))[1:], reverse=True)
    largest_gap = max([a - b for a, b in zip(n_list, n_list[1:])])
    max_n = max(n_list)
    min_n = min(n_list)
    print(f"Max {max_n}, Min {min_n}, Largest gap {largest_gap}")