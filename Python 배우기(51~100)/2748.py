n = int(input())
f_list = [0, 1]
for i in range(n):
    current = f_list[i] + f_list[i+1]
    f_list.append(current)

print(f_list[n])