import sys

num = int(sys.stdin.readline().strip())



new_num = (num%10)*10+((num//10) + (num%10))%10
ans = 1
while num != new_num:
    new_num = (new_num%10)*10+((new_num//10) + (new_num%10))%10
    ans +=1

print(ans)
