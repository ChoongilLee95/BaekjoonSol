import sys

input = sys.stdin.readline

num_num = int(input().strip())

nums = list(map(int, input().strip().split()))

operator = list(map(int,input().strip().split()))

num_list = []

def dfs(idx,answer):
    if idx == num_num:
        num_list.append(answer)
    else:
        tmp = nums[idx]
        for i in range(4):
            ans = answer
            if operator[i] >0:
                operator[i] -= 1
                if i == 0:
                    ans += tmp
                elif i == 1:
                    ans -= tmp
                elif i ==2:
                    ans *=tmp
                else:
                    if ans < 0:
                        ans = -(-ans//tmp)
                    else:
                        ans = ans//tmp
                dfs(idx+1,ans)
                operator[i]+=1
dfs(1,nums[0])
for i in range(len(num_list)):
    if i:
        max_num = num_list[i] if num_list[i] > max_num else max_num
        min_num = num_list[i] if num_list[i] < min_num else min_num
    else:
        max_num = num_list[i]
        min_num = num_list[i]
print(max_num)
print(min_num)

