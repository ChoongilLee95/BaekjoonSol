import sys

def interval(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return target-1
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    a = interval(start, mid, index * 2, left, right)//(start-mid+1)
    b = interval(mid + 1, end, index * 2 + 1, left, right)
    


def init(start, end, index):
    # 가장 끝에 도달했으면 arr 삽입
    if start == end:
        tree[index] = boxes[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
    left = init(start, mid, index * 2)
    right = init(mid + 1, end, index * 2 + 1)
    tree[index] = (start-end+1)*left if left<right else (start-end+1)*right
    return tree[index]
boxes  = list(map(int,sys.stdin.readline().strip().split()))

while boxes[0]:
    tree = [0]*(boxes[0]*4)
    right = boxes[0]
    init(1,right,1)
    ans = right
    for i in range(1,right+1):
        if boxes[i] !=1:
            for j in range(right-i+1):
                if boxes[i+j] ==1:
                    break
                target = ans//(j+1) +1
                new_ans =  (j+1)*interval(1,right,1,i,i+j,target)
                if new_ans>ans:
                    ans = new_ans
    print(ans)
    boxes  = list(map(int,sys.stdin.readline().strip().split()))

