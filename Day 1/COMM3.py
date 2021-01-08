# Implemented Using 1-D Array
# Can also be done with 2-D Arrays
# Remember --> Always use square instead of
# Square root. Because computer will have to face floating point
# Comparison in which it is not that good.
def chk(arr,r):
#    i = 0 ; j = 1
    dis = []
    for i in range(0,3,2):
        for j in range(i+2,6,2):
            dis.append( (arr[i] - arr[j])**2 + (arr[i+1]-arr[j+1])**2)
            #print("temp is",temp)
            #dis.append(temp)

#    m = max(dis)
    #print("dis is",dis)
    #print("r is",r)
    if (dis[0]<=r*r and dis[1]<=r*r)or(dis[0]<=r*r and dis[2]<=r*r)or(dis[1]<=r*r and dis[2]<=r*r):
        return "yes"
    return "no"

t = int(input())
while(t>0):
    r = int(input().split()[0])
    n = []
    for i in range(3):
        n.extend(list(map(int,input().split())))
   # print("n is",n)
    print(chk(n,r))
    t-=1
