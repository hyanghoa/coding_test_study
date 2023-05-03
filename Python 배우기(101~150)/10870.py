n = int(input())
fibonacci = [0, 1]
while len(fibonacci) <= n:
    fibonacci.append(sum(fibonacci[-2:]))
print(fibonacci[n])