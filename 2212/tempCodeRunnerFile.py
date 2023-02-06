import sys

input = sys.stdin.readline

N = int(input())

K = int(input())

sensors = list(map(int, input().strip().split()))

sensors.sort()

len_senser = sensors[-1] - sensors[0]
max_senser_by_one = len_senser//K-1
if len_senser%K:
    max_senser_by_one +=1

new_start = sensors[0]
covered_by_one = 0
ans = 0
for i in range(N):
    if sensors[i]-new_start > max_senser_by_one:
        ans += sensors[i-1] - new_start
        new_start = sensors[i]
    
ans +=sensors[-1] - new_start

print(ans)

