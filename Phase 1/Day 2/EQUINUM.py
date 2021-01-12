# Find equilibrium number from an array.
# Equi num is such that
# lsum = rsum
# Make use of a prefix sum array.

def equi(a):
    sum = 0
    for i in a :
        sum += i
    lsum = a[0]
    for i in range(1,len(a)-1):
        if lsum == sum - a[i] -lsum :
            return a[i]
        lsum += a[i]
    return "NO EQUILIBRIUM"

for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(equi(arr))
