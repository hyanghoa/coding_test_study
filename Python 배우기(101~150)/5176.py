for _ in range(int(input())):
    p, m = map(int, input().split())
    visit_list = [True] * m
    answer = 0
    
    for _ in range(p):
        n = int(input())
        if visit_list[n-1]:
            visit_list[n-1] = False
        else:
            answer += 1
            
    print(answer)