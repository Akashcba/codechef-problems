# Character Check in a string.
def chk(a):
    for i in a:
        if i == 'Y':
            return "NOT INDIAN"
        elif i == 'I':
            return "INDIAN"
    return "NOT SURE"

t = int(input())
while(t>0):
    n = int(input())
    seq = input().split()[0]
    print(chk(seq))
    t-=1
