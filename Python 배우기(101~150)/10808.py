from string import ascii_lowercase


string = input()
answer = {x: 0 for x in ascii_lowercase}
for s in string:
    answer[s] += 1
print(*answer.values())