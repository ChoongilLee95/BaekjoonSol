import sys

def main(n,li):
    white = 0
    blue = 0
    def makelower():
        nonlocal n
        n = n//2
        new_li =[[0]*(n) for _ in range(n)]
        for y in range(n):
            for x in range(n):
                new_li[y][x]=smallbox(2*y,2*x)
        return new_li
    def smallbox(y,x):
        nonlocal blue
        nonlocal white
        nums_list = [li[y][x],li[y+1][x],li[y+1][x+1],li[y][x+1]]
        if li[y][x]*li[y+1][x]*li[y+1][x+1]*li[y][x+1]==1:
            return 1
        elif sum(nums_list) ==0:
            return 0
        else:
            for i in nums_list:
                if i==1:
                    blue+=1
                elif i ==0:
                    white +=1
            return 2
    while n>1:
        li = makelower()
        # for i in range(n):
        # print(f'white = {white}')
        # print(f'blue = {blue}')
    if li[0][0] == 0:
        white +=1
    elif li[0][0]==1:
        blue +=1
    print(white)
    print(blue)


num = int(sys.stdin.readline().strip())
num_list = []
for _ in range(num):
    num_list.append(list(map(int, sys.stdin.readline().strip().split())))

main(num, num_list)