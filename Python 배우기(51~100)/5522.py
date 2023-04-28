total_score = 0
for _ in range(100):
    try:
        total_score += int(input())
    except:
        pass
print(total_score)