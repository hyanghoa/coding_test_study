from itertools import combinations


formula = input()
index_list = []
stack = []
for idx, f in enumerate(formula):
    if f == "(":
        stack.append(idx)
    elif f == ")" and stack:
        index_list.append((stack.pop(), idx))
    
answer = []
for i in range(1, len(index_list)+1):
    for comb in combinations(index_list, i):
        formula_list = list(formula)
        for c in comb:
            formula_list[c[0]] = ""
            formula_list[c[1]] = ""
        answer.append("".join(formula_list))
    
for ans in sorted(set(answer)):
    print(ans)