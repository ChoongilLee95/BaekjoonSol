import sys

def mini(li,left,right, target):
    ans = li[right]
    for i in range(left,right):
        if ans <target:
            break
        if li[i]<ans:
            ans = li[i]
    return ans

boxes  = list(map(int,sys.stdin.readline().strip().split()))

while boxes[0]:
    tree = [0]*(boxes[0]*4)
    right = boxes[0]
    ans = right
    for i in range(1,right+1):
        if boxes[i] !=1:
            for j in range(right-i+1):
                if boxes[i+j] ==1:
                    break
                target = ans//(j+1)+1
                new_ans =  (j+1)*mini(boxes,i,i+j,target)
                if new_ans>ans:
                    ans = new_ans
    print(ans)
    boxes  = list(map(int,sys.stdin.readline().strip().split()))
