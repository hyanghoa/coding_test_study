hour, minute = map(int, input().split())
hour *= 60
total = hour + minute - 45
hour = total//60%24
minute = total%60
print(hour, minute)