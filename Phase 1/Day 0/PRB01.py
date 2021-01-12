# Primality Check of a Number.
def status(a):
    if a < 2:
        return 'no'
    elif a ==2:
        return 'yes'
    for i in range(2,int(a**1/2) + 1 ):
        if a%i==0:
            return 'no'
    return 'yes'
t = int(input())
while t>0  :
    n =int(input())
    print(status(n))
    t-=1
