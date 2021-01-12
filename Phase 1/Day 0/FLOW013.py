# program to check whether a triangle is valid or not.
# The three angles of the triangle are inputs.

def chk(ls):
    return (ls[0]+ls[1]+ls[2])==180

t = int(input())
while(t>0):
    inp = list(map(int,input().split()))
    print(["YES" if chk(inp)==1 else "NO"])
    t-=1
