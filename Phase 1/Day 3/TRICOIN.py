# cook your dish here
import math
def count(a):
    if a == 1:
        return 1
## n(n+1)/2 == a
## n^2 + n -2a = 0
## D = 1^2 - 4(-2a)1
##(-1 + sqrt(1 + 8a))//2
    return int((-1 + math.sqrt(1 + 8*a))/2)

def main():
    t = int(input())
    while(t>0):
        t-=1
        n = int(input())
        print(count(n))

if __name__ =='__main__':
    main()
