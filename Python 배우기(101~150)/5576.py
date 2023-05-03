w_score_list, k_score_list = [], []
for i in range(20):
    if i < 10:
        w_score_list.append(int(input()))
    else:
        k_score_list.append(int(input()))
        
print(sum(sorted(w_score_list)[-3:]), sum(sorted(k_score_list)[-3:]))