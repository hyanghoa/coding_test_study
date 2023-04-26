s = int(input())
n = 1
n_sum = 0

while True:
    if (n_sum + n) > s:
        break
    n_sum += n
    n += 1
print(n-1)