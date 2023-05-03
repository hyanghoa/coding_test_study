s = input()
count_dict = {x.upper(): 0 for x in set(list(s))}
for x in s:
    count_dict[x.upper()] += 1

answer = (sorted(count_dict.items(), key=lambda x: x[1]))
if len(answer) != 1 and answer[-1][1] == answer[-2][1]:
    print("?")
else:
    print(answer[-1][0])