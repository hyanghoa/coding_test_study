string_list = []
while True:
    string = input()
    if string == "END":
        break
    string_list.append(string)
    
for s in string_list:
    print(s[::-1])