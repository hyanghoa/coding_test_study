for _ in range(int(input())):
    parenthesis_list = []
    answer = ""
    
    for s in input():
        if s == "(":
            parenthesis_list.append(s)
        else:
            if parenthesis_list:
                parenthesis_list.pop()
            else:
                answer = "NO"
            
    if parenthesis_list:
        print("NO")
    elif answer == "NO":
        print(answer)
    else:
        print("YES")