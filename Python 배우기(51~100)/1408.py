current_time = list(map(int, input().split(":")))
start_time = list(map(int, input().split(":")))
current_time = current_time[0]*60*60 + current_time[1]*60 + current_time[2]
start_time = start_time[0]*60*60 + start_time[1]*60 + start_time[2] + 24*60*60
answer = start_time - current_time
print(f"{answer//60//60%24:02d}:{answer//60%60:02d}:{answer%60:02d}")