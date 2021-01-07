# Game Theory Application Example
def win(a,b,n):
# After making table
# The following logic will be formed ...
# If n is even return max(a,b)//min(a,b)
# If n is odd return max(2*a,b)//min(2*a,b)
    if n%2 ==0:
        return max(a,b)//min(a,b)
    else :
        return max(2*a,b)//min(2*a,b)

t = int(input())
while(t>0):
    inp = list(map(int,input().split()))
# A, B, N == test Case input structure
# Draw the table of output containing Ai and Bi
# for i = 8

    print(win(inp[0],inp[1],inp[2]))
    t-=1
