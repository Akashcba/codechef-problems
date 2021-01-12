# Finding Square root
# Using binary search
# Upto closest integer

def fsqrt(a):
    start = 0
    end = a
    ans = 0

    while(start <= end):
        mid = (start+end)//2
        if mid*mid == a:
            return mid
        elif mid*mid > a:
            end = mid -1
        else :
            start = mid +1
            ans = mid
    return ans

for i in range(int(input())):
    n = int(input())
    print(fsqrt(n))
