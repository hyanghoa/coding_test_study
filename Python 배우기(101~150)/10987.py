string_list = list(input())
answer = 0
for x in ["a", "e", "i", "o", "u"]:
    answer += string_list.count(x)
    
print(answer)