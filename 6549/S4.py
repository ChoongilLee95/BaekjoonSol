import sys
sys.setrecursionlimit(10**6)
def devide_conquer(left,right):
    if left == right:
        return boxes[left]
    mid = (left+right)//2
    lc = mid
    rc = mid+1
    min_h = min(boxes[lc],boxes[rc])
    tmp = min_h*2
    span = 2
    while True:
        if lc>left and rc<right:
            if boxes[lc-1] > boxes[rc+1]:
                lc-=1
                min_h = min_h if min_h < boxes[lc] else boxes[lc]
                span +=1
            else:
                rc +=1
                if boxes[rc]:
                    min_h = min_h if min_h < boxes[rc] else boxes[rc]
                    span +=1
                else:
                    break
        elif lc>left:
            lc-=1
            if boxes[lc]:
                min_h = min_h if min_h < boxes[lc] else boxes[lc]
                span +=1
            else:
                break
        elif rc<right:
            rc +=1
            if boxes[rc]:
                min_h = min_h if min_h < boxes[rc] else boxes[rc]
                span +=1
            else:
                break
        else:
            break
        tmp = max(tmp,span*min_h)
    return max(devide_conquer(left,mid),devide_conquer(mid+1,right),tmp)


boxes  = list(map(int,sys.stdin.readline().strip().split()))

while boxes[0]:
    print(devide_conquer(1,boxes[0]))
    boxes  = list(map(int,sys.stdin.readline().strip().split()))

