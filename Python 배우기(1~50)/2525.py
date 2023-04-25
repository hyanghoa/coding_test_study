a, b = map(int, input().split())
c = int(input())
total = a*60 + b + c
hour = total//60%24
minuite = total%60
print(hour, minuite)