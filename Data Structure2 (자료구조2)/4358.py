import sys


tree_dict = {}
for i in range(1000000):
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    elif tree_dict.get(tree) is not None:
        tree_dict[tree] += 1
    else:
        tree_dict[tree] = 1
        
for key in sorted(tree_dict):
    print(f"{key} {tree_dict[key]/i*100:.4f}")