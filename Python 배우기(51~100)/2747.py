n = int(input())
fibonacci = [0, 1]
for i in range(2, n+1):
    fibonacci.append(sum(fibonacci[i-2:]))
print(fibonacci[n])