import sys
N,r,c = map(int, sys.stdin.readline().strip().split())

def Z_line(N,r,c):
    if N==1:
        return c+r*2
    new_row = r%(2**(N-1))
    new_colume = (c)%(2**(N-1))
    how_much = (((r//(2**(N-1)))*2 +c//(2**(N-1))))*2**(2*N-2)
    return how_much + Z_line(N-1,new_row,new_colume)
print(Z_line(N, r, c))

