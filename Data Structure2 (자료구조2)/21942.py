import sys
from datetime import datetime


n, l, f = input().split()
n = int(n)
f = int(f)
rental = {}
answer = {}
for _ in range(n):
    date, time, p, m = sys.stdin.readline().split()
    if rental.get(f"{p}/{m}") is not None:
        rental_year, rental_month, rental_day = rental.get(f"{p}/{m}")[0].split("-")
        rental_hour, rental_minute = rental.get(f"{p}/{m}")[1].split(":")
        return_year, return_month, return_day = date.split("-")
        return_hour, return_minute = time.split(":")
        rental_date = datetime(int(rental_year), int(rental_month), int(rental_day), int(rental_hour), int(rental_minute))
        return_date = datetime(int(return_year), int(return_month), int(return_day), int(return_hour), int(return_minute))
        deadline = list(map(int, l.replace(":", "/").split("/")))
        deadline = deadline[0]*24*60*60 + deadline[1]*60*60 + deadline[2]*60
        if (return_date-rental_date).total_seconds() > deadline:
            if answer.get(m) is not None:
                answer[m] += int(((return_date-rental_date).total_seconds()-deadline)//60*f)
            else:
                answer[m] = int(((return_date-rental_date).total_seconds()-deadline)//60*f)
        rental.pop(f"{p}/{m}")
    else:
        rental[f"{p}/{m}"] = (date, time)
if answer:
    for ans in sorted(answer.items()):
        print(*ans)
else:
    print(-1)