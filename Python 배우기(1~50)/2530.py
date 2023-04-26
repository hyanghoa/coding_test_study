a, b, c = map(int, input().split())
d = int(input())
total = a*60*60 + b*60 + c + d
hour = total//60//60%24
minuite = total//60%60
second = total%60
print(hour, minuite, second)