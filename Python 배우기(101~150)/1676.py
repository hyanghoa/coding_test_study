factorial = 1
for i in range(1, int(input())+1):
    factorial *= i

answer = 0
for s in str(factorial)[::-1]:
    if s == "0":
        answer += 1
    else:
        break
print(answer)