import sys
def each(c,r):
    a1 = nums[c][r]
    a2 = nums[c][r+1]
    a3 = nums[c+1][r]
    a4 = nums[c+1][r+1]
    if a1 == a2 == a3 == a4 =='0':
        return '0'
    elif a1 == a2 == a3 == a4 =='1':
        return '1'
    else:
        return f'({a1}{a2}{a3}{a4})'

def make_new(n):
    new_nums = []
    for col in range(n//2):
        new_col = []
        for row in range(n//2):
            new_col.append(each(2*col,2*row))
        new_nums.append(new_col)
    return new_nums
nums = []
n  = int(sys.stdin.readline().strip())
for i in range(n):
    nums.append(list(sys.stdin.readline().strip()))
print(nums)
while n>1:
    nums = make_new(n)
    n//=2
print(nums[0][0])

