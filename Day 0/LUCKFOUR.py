# Matching 4 in a Number
# Although number can saved as string but
# We will be storing it as integer only.

def chk(a):
    count = 0
    while(a>0):
        temp = a%10
        if temp == 4: count+=1
        a = a//10
    return count

t = int(input())
while(t>0):
    n = int(input())
    print(chk(n))
    t-=1
