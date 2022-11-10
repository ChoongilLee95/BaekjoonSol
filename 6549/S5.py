import sys

def max_area():
    stack = []
    tmp = 0
    for i in range(1,boxes[0]+1):
        if len(stack):
            while boxes[stack[-1]]> boxes[i]:
                idx = stack.pop()
                if len(stack):
                    tmp = max(tmp,(i-stack[-1]-1)*boxes[idx])
                else:
                    tmp = max(tmp,(i-1)*boxes[idx])
                    break
        stack.append(i)
    while len(stack):
        idx = stack.pop()
        if len(stack):
            tmp = max(tmp,(boxes[0]-stack[-1])*boxes[idx])
        else:
            tmp = max(tmp,(boxes[0])*boxes[idx])
            break
    return tmp

boxes  = list(map(int,sys.stdin.readline().strip().split()))
while boxes[0]:
    print(max_area())
    boxes  = list(map(int,sys.stdin.readline().strip().split()))

