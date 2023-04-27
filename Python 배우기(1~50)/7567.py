inputs = input()
previous = inputs[0]
answer = 10
for x in inputs[1:]:
    if previous != x:
        answer += 10
    else:
        answer += 5
    previous = x
print(answer)