# Maximum no. of squares of side 2x2
# that can fit an isosceles triangle
# Given input is the base of this triangle
# f(b) = (b/2 -1) + f(b-2)
# f(1)=f(2)=f(3) = 0
# Modified version of Fibonacci Numbers.
def tri(a):
    if a <= 3:
        return 0
#    else:
#        return (a//2 -1 ) + tri(a-2)
# Only recursion tree size allowed = 8
# So go for iterative way
    ans = 0
    while a > 3:
        ans += a//2 -1
        a -=2
    return ans

t = int(input().split()[0])
while(t>0):
    n = int(input())
    print(tri(n))
    t-=1
