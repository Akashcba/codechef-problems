# R + B = G
# B + G = R
# G + R = B

def col(a,n):
    ls = {'R':0,'G':0,'B':0 } # [ R, G ,B ]
    for i in a :
        ls[i] += 1
    return n - max(ls.values())


def main():
    t = int(input())
    while(t>0):
        t-=1
        n = int(input())
        s =input().split(" ")[0]
        print(col(s,n))


if __name__ == "__main__":
    main()
