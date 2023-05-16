brackets = input()
brackets = brackets.replace("()", "|")
stack = []
answer = 0
for idx, x in enumerate(brackets):
    if x == "|":
        answer += len(stack)
    elif x == "(":
        stack.append(idx)
    else:
        stack.pop()
        answer += 1
print(answer)