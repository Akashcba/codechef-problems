# Maximal l*r value
# If there is clash -> with max Ri
# If again clash there smaller index
def chk(a,b,n):
    max_m = 0; ind = 0
    for i in range(n):
        m = a[i] * b[i]
        if m > max_m :
            max_m = m
            ind = i
        elif m == max_m:
            if b[i] > b[ind]:
                    ind = i
    return ind + 1

def main():
    t = int(input())
    while(t>0):
        try:
            t-=1
            n = int(input())
            l = list(map(int,input().split()))
            r = list(map(int,input().split()))
            print(chk(l,r,n))
        except :
            pass


if __name__ == '__main__':
    main()
