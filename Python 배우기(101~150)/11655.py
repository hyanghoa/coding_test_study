from string import ascii_lowercase


alphabet_base_dict = {s: idx for idx, s in enumerate(ascii_lowercase)}
number_base_dict = {idx: s for idx, s in enumerate(ascii_lowercase)}
answer = ""
for x in input():
    if x != " " and not x.isnumeric():
        if x.isupper():
            index = (alphabet_base_dict[x.lower()] + 13) % 26
            answer += number_base_dict[index].upper()
        else:
            index = (alphabet_base_dict[x] + 13) % 26
            answer += number_base_dict[index]
    else:
        answer += x
print(answer)