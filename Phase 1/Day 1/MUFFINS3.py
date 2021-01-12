# Choose a number b/w 1 and n both inclusive
# We need to give the max value of N % A
# N is the number of cakes availble with us.
# So we can get max value of N % A
# which is given by the expression
# floor(N/2 + 1)

import math

def chk(a):
    return math.floor(a/2 + 1)

t = int(input())
while(t>0):
    n = int(input())
    print(chk(n))
    t-=1
# Eg : N = 5
# A = 1 -> N%A = 0
# A = 2 -> N%A = 1
# N = 3 -> N%A = 2  ---> MAX VALUE POSSIBLE
# N = 4 -> N%A = 1
