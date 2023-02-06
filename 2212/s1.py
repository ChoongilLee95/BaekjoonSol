import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
sensors = list(map(int, input().strip().split()))
sensors.sort()
nums = []
for i in range(1,N):
    nums.append(sensors[i]-sensors[i-1])
nums.sort()
ans = 0
for i in range(N -K):
    ans+=nums[i]
print(ans)
