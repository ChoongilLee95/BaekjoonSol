import sys


##[[x1, y1][x2,y2]]
def find_touched(test,big):
    global buildings
    new_test = []
    for i in test:
        buildings[i[0]][i[1]] -=1
        big+=1
        if -1<i[0]-1:
            if buildings[i[0]-1][i[1]]==0:
                new_test.appned([i[0]-1,i[1]])
        if i[0]+1<num:
            if buildings[i[0]+1][i[1]]==0:
                new_test.appned([i[0]+1,i[1]])
        if i[1]-1>-1:
            if buildings[i[0]][i[1]-1]==0:
                new_test.appned([i[0],i[1]-1])
        if i[1]+1<num:
            if buildings[i[0]][i[1]+1]==0:
                new_test.appned([i[0],i[1]+1])
    if new_test==[]:
        return big
    return find_touched(new_test,big)


num  = int(sys.stdin.readline().strip())
nums = range(num)

buildings = []
for i in range(num):
    new_row = list(map(int,sys.stdin.readline().strip().split()))
    buildings.append(new_row)
ans = 0
for i in range(100):
    biggest =0
    new_ans = 0
    danger_zone = [[0]*num for _ in range(num)]
    for r in nums:
        for c in nums:
            buildings[r][c] -=1
    for r in nums:
        for c in nums:
            if danger_zone[r][c]:
                continue
            else:
                new_big = find_touched([[r,c]],0)
                if new_big > biggest:
                    biggest = new_big
                new_ans +=1

    if new_ans>ans:
        ans = new_ans
    if biggest <3:
        break

print(ans)