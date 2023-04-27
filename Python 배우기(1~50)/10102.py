v = int(input())
votes = input()
result = {"A": 0, "B": 0}
for vote in votes:
    result[vote] += 1

if result["A"] > result["B"]:
    print("A")
elif result["A"] < result["B"]:
    print("B")
elif result["A"] == result["B"]:
    print("Tie")