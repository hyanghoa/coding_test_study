string = input()
answer = ""
for s in string:
    if s.isupper():
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)