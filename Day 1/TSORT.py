# Modified Implementation of
# Count sort
import numpy as np
def count(a,i):
    k = np.zeros(i+1)
    ans = []
    for j in a:
        k[j] += 1
    for j in range(i+1):
        if k[j]:
            for m in range(int(k[j])):
                ans.append(j)
    return list(map(str,ans))
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
