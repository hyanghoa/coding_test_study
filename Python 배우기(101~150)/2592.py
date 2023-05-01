from collections import Counter


n_list = []
for _ in range(10):
    n_list.append(int(input()))
    
print(sum(n_list)//len(n_list))
print(Counter(n_list).most_common(1)[0][0])