def avg(a,n):
    ans = 0
    for i in a:
        ans += i
    return ans/n


def chk(a,n):
    if 2 in a :
        return "No"
    elif 5 not in a:
        return "No"
    elif avg(a,n) < 4.0 :
        return "No"
    return "Yes"

def main():
    t = int(input())
    while(t>0):
        t-=1
        n = int(input())
        s = list(map(int,input().split()))
        print(chk(s,n))

if __name__ == "__main__":
    main()
