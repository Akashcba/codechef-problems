
def chk(a,q,n):
    l = a[0]
    m = a[n - 1]
    if q >= l and q <= m :
        return("Yes")
    return "No"
def main():
    n,q=map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    while(q > 0):
        q-=1
        ques = int(input())
        print(chk(A,ques,n))

if __name__ == "__main__":
    main()
