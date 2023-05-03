from string import ascii_uppercase


alphabet_dict = {x: idx+1 for idx, x in enumerate(ascii_uppercase)}
for _ in range(int(input())):
    string_list = input().split()
    answer = []
    for x, y in zip(string_list[0], string_list[1]):
        if alphabet_dict[x] <= alphabet_dict[y]:
            answer.append(alphabet_dict[y] - alphabet_dict[x])
        else:
            answer.append(26 + alphabet_dict[y] - alphabet_dict[x])
    print(f"Distances: {' '.join(map(str, answer))}")