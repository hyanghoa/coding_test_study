n_list = []
for _ in range(5):
    n_list.append(int(input()))
print(min(n_list[:3])+min(n_list[3:])-50)