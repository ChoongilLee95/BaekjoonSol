import sys

len_day,len_night,len_bar  = map(int, sys.stdin.readline().strip().split())

margin = len_bar - len_day-1

per_day = len_day - len_night

ans = margin//per_day +2

print(ans)
