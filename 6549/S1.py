import sys

def mini(li,left,right):
    ans = li[right]
    for i in range(left,right):
        if ans ==1:
            break
        if li[i]<ans:
            ans = li[i]
    return ans

boxes  = list(map(int,sys.stdin.readline().strip().split()))

while boxes[0]:
    left = 1
    right = boxes[0]
    sqr = right-left+1
    while left <=right:
        new_sqr = (right-left+1)*mini(boxes,left,right)
        if new_sqr>sqr:
            sqr = new_sqr
        if boxes[left]>boxes[right]:
            right-=1
        elif boxes[left]<boxes[right]:
            left+=1
        else:
            left+=1
            right-=1
    boxes  = list(map(int,sys.stdin.readline().strip().split()))
    print(sqr)

