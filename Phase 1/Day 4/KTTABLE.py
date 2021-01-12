
def chk(a,b,n):
    t = 0 ;count = 0
    for i in range(n):
        t = a[i] - t
        if b[i] <= abs(t):
            count+=1
        t = a[i]
    return count

def main():
    t =int(input())
    while(t>0):
        t-=1
        n =int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        print(chk(a,b,n))


if __name__=="__main__":
    main()
