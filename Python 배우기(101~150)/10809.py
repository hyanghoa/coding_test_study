from string import ascii_lowercase


string = input()
string_dict = {x: string.find(x) for x in list(ascii_lowercase)}
print(*string_dict.values())