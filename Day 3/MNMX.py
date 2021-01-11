def chk(a):
    if len(a) == 2: return 1 ;
    m = min(a)
    return (len(a) - 1)*m


def main():
    t = int(input())
    while(t>0):
        t-=1
        n = int(input())
        ls = list(map(int,input().split(" ")))
        print(chk(ls))
if __name__ == '__main__':
    main()
    
