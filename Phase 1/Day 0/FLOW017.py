# Program to find 2nd largest
# number among 3 numbers entered by the user.

def sec_largest(a,b,c):
    smallest = min(min(a, b), c)
    # min(a,b,c) is allowed in python.
    largest = max(max(a, b), c)
    # max(a,b,c) valid in python
    return a ^ b ^ c ^ smallest ^ largest
    # Method to arrange elements

t = int(input())

while t>0:
    inp = list(map(int,input().split()) )
    print(sec_largest(inp[0],inp[1],inp[2]) ,sep ='')
    t-=1
