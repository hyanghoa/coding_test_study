a = 60 * 5
b = 60
c = 10
t = int(input())

answer = {
    "a": 0,
    "b": 0,
    "c": 0,
}
for key in answer:
    if key == "a" and a <= t:
        answer[key] += t // a
        t %= a
    elif key == "b" and b <= t:
        answer[key] += t // b
        t %= b
    elif key == "c" and c <= t:
        answer[key] += t // c
        t %= c
        
if t > 0:
    print(-1)
else:
    print(*answer.values())