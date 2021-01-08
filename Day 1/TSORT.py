# Modified Implementation of
# Count sort

def count(ab,i):
    c = [0]*(i+1) ## Valid
    #print("c is",c)
    for j in ab:
        c[j] += 1
    k = 0
    a = [0]*len(ab) ## Valid
    for j in range(i+1):
        if c[j] :
            for m in range(c[j]):
                a[k] = j
                k += 1
    return a
t =int(input())
n = []
while(t>0):
    n.append(int(input()) )
    t-=1
n = count(n,max(n))
for i in n:
    print(i)
# Naive approach applied here
# Best implementation look at gfg for count sort...
