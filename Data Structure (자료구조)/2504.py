brackets = input()
stack = []
tmp = []
answer = 0
last_bracket = ""
for bracket in brackets:
    if bracket == "(" or bracket == "[":
        stack.append(bracket)
        if len(stack) > len(tmp):
            tmp.append(0)
            
    elif bracket == ")" or bracket == "]":
        if stack:
            stack_pop = stack.pop()
        else:
            answer = 0
            stack = []
            tmp = []
            break
        
        if stack_pop == "(" and bracket == ")":
            n = 2
        elif stack_pop == "[" and bracket == "]":
            n = 3
        else:
            answer = 0
            stack = []
            tmp = []
            break

        if last_bracket == ")" or last_bracket == "]":
            tmp[len(stack)] += tmp.pop()*n
        else:
            tmp[len(stack)] += n
            
    last_bracket = bracket

answer += sum(tmp)
if stack:
    print(0)
else:
    print(answer)