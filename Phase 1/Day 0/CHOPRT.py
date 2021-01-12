# Relational Operators
t = int(input())
while(t>0):
    n = list(map(int,input().split()))
    #print("n is",n)
    if n[0] < n[1]:
        print("<")
    elif n[0] > n[1]:
        print(">")
    else :
        print("=")
    t-=1
