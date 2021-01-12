# Check if a sequence of numbers is palindrome or not.
# Palindrome Check .....
def chk(a):
    i ,j = 0,len(a) - 1
    while(i<j):
        if a[i] != a[j]:
            return "loses"
        i+=1
        j-=1
    return "wins"

t = int(input())
while(t>0):
    n = input().split(' ')[0]
    #print("n is ",n)
    print(chk(n))
    t-=1
