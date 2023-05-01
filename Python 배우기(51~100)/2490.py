answer_dict = {
    4: "E",
    3: "A",
    2: "B",
    1: "C",
    0: "D",
}
for _ in range(3):
    n_list = list(map(int, input().split()))
    print(answer_dict[sum(n_list)])