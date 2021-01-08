# Print factorial of the input number
# Not going with recursive approach
# because the max size of heap space is 8
# in the platform ide .

def fact(a):
    if a <= 1: return 1
    ans = 1
    while a > 1:
        ans *= a
        a -=1
    return ans

t =int(input())
while t >0:
    n = int(input())
    print(fact(n))
    t-=1
