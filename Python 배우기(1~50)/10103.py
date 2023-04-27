t = int(input())
a_score = 100
b_score = 100

for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        b_score -= a
    elif a < b:
        a_score -= b

print(a_score)
print(b_score)