import sys

input =sys.stdin.readline

target = int(input())

num_rel = int(input())
# 메모이제이션
dp = [[0]*(target+1) for _ in range(target+1)]

# 제료인지, 즉 끝단인지 -> 사실 분류안해도 되지만, 끝단을 조회하며 dp(메모이제이션)을 만들어주는건 비효율
# 단 끝단 직전에서 끝단으로 넘어가기 전에 판단을 해야한다.
jeryo = [True]*(target+1)

# 작업이 완료 되었는지 확인 끝단도 False지만 jeryo로 안넘어가게 만들어준다.
done = [False]*(target+1)

for _ in range(num_rel):
    making,maker,num = map(int,input().split())
    dp[making][maker]=num
    # 이렇게 하면 재료 즉 끝단만 True
    jeryo[making] = False

def dp(n):
    if done[n]:
        return dp[n]
    for idx_n in range(1,target+1):
        if dp[n][idx_n] == 0 or jeryo[idx_n]:
            continue
        arr = dp(idx_n)
        for idx_next in range(1,target+1):
            dp[n][idx_next] += arr[idx_next]*dp[n][idx_n]
        dp[n][idx_n] = 0
    done[n] = True
    return dp[n]
answer = dp(target)
for i in range(1,target+1):
    if answer[i]:
        print(i,answer[i])
