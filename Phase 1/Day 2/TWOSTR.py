
def chk(a,b):
    j ,i = 0,0
    while(i < len(a) and j < len(b)):
        if a[i] == '?' or b[j] == '?':
            i+=1
            j+=1
        elif a[i] == b[j]:
            i+=1
            j+=1
        else :
            return "No"
    return "Yes"


for i in range(int(input())):
    a = input().split(" ")[0]
    b = input().split(" ")[0]
    print(chk(a,b))
