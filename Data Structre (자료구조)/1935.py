t = int(input())
operators = [ord(x)-65 for x in input()]
nums = [int(input()) for i in range(t)]
answer = []
for op in operators:
    if op < 0:
        op = chr(op+65)
        if op == "*":
            b, a = answer.pop(), answer.pop()
            answer.append(a*b)
        elif op == "/":
            b, a = answer.pop(), answer.pop()
            answer.append(a/b)
        elif op == "+":
            b, a = answer.pop(), answer.pop()
            answer.append(a+b)
        elif op == "-":
            b, a = answer.pop(), answer.pop()
            answer.append(a-b)
    else:
        answer.append(nums[op])
        
print(f"{answer[0]:.2f}")