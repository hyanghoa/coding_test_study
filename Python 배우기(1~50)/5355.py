t = int(input())
for _ in range(t):
    input_list = input().split()
    input_list[0] = float(input_list[0])
    for x in input_list[1:]:
        if x == "@":
            input_list[0] *= 3
        elif x == "%":
            input_list[0] += 5
        elif x == "#":
            input_list[0] -= 7
    print(f"{input_list[0]:.2f}")