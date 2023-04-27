t = int(input())
for _ in range(t):
    ox = input()
    score = 0
    score_sum = 0
    
    for x in ox:
        if x == "O":
            score += 1
        else:
            score = 0
        score_sum += score
        
    print(score_sum)