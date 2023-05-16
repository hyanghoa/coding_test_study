n, k = map(int, input().split())
n_list = [i+1 for i in range(n)]
answer = []
current_index = 0
for i in range(1, n+1):
    current_index += k - 1
    current_index %= len(n_list)
    answer.append(str(n_list.pop(current_index)))
print(f"<{', '.join(answer)}>")