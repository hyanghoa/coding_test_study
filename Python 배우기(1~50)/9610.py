result = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0,
    "AXIS": 0,
}
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        result["AXIS"] += 1
    elif a > 0 and b > 0:
        result["Q1"] += 1
    elif a < 0 and b > 0:
        result["Q2"] += 1
    elif a < 0 and b < 0:
        result["Q3"] += 1
    elif a > 0 and b < 0:
        result["Q4"] += 1

for k, v in result.items():
    print(f"{k}: {v}")