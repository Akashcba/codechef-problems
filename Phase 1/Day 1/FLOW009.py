

t = int(input())
while(t>0):
    t-=1
    q,p = map(float,input().split())
    print("{0:.6f}".format(*[q*p if q < 1000 else q*p*0.90 ]) )
# * is a universal unpacker
