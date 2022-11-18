import sys

input  = sys.stdin.readline

test = [5,3,2,6,7,15]

case_1 = [4,3,1,1] # 7,6,3,2
case_2 = [1,1,1,1] # 3,2,7,6
case_3 = [4,3,2,1] # 7,6,2,3

ans = 0
for i in case_1:
    ans+= test[i-1]*test[i]*test[i+1]
    print(test[i-1],test[i],test[i+1],'=',test[i-1]*test[i]*test[i+1])
    test.pop(i)
print(ans)
ans = 0
test = [5,3,2,6,7,15]

for i in case_2:
    ans+= test[i-1]*test[i]*test[i+1]
    print(test[i-1],test[i],test[i+1],'=',test[i-1]*test[i]*test[i+1])
    test.pop(i)
test = [5,3,2,6,7,15]

print(ans)
ans = 0

for i in case_3:
    ans+= test[i-1]*test[i]*test[i+1]
    print(test[i-1],test[i],test[i+1],'=',test[i-1]*test[i]*test[i+1])
    test.pop(i)
print(ans)
