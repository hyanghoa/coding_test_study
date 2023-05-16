formular = input()
stack = []
answer = ""
for idx, f in enumerate(formular):
    if f.isalpha():
        answer += f
    else:
        if f == "(":
            stack.append(f)
        elif f == ")":
            while stack:
                s = stack.pop()
                if s == "(":
                    break
                answer += s
        elif f == "*" or f == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(f)
        elif f == "+" or f == "-":
            while stack and (stack[-1] != "("):
                answer += stack.pop()
            stack.append(f)
        else:
            stack.append(f)
        
while stack:
    answer += stack.pop()
print(answer)