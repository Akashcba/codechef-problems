
def chk(a,b,n):
    count1 =0 ;count2 =0
    for i in a:
        if i in b :
            count1 +=1
    for i in range(1,n+1):
        if i not in a and i not in b :
            count2+=1
    return str(count1 )+' '+ str(count2)

def main():
    t = int(input())
    while(t>0):
        t-=1
        n,m,k= map(int,input().split())
        ig = list(map(int,input().split()))
        tr = list(map(int,input().split()))
# No. of source files -> tracked and ignored --> Intersection
# No. of files -> both untracked and unignored.
        print(chk(ig,tr,n))

if __name__ =='__main__':
    main()
