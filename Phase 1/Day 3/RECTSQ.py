# Minimum plots = area / area(gcd(m,n))


def gcd(a,b):
    while(a!=b):
        if a>b:
            a = a - b
        else :
            b = b - a
    return a


def main():
    t = int(input())
    while(t>0):
        t-=1
        n,m=map(int,input().split())
        print((n*m)//gcd(n,m)**2)

if __name__ == "__main__":
    main()
