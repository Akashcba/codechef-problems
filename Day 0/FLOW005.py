# Sum of Rs. N given.
# Program to compute smallest number of notes
# that combine to give Rs. N
# Available notes : 1, 2, 5, 10, 50, 100

def chk(rs):
    ls = [100,50,10,5,2,1]
    count = 0
    for i in ls:
        if rs >= i:
            count += rs//i
            rs = rs%i
    return count


t = int(input())
#print("t is",t)
while(t>0):
    n = list(map(int,input().split()) )
    #print("n is",n[0])
    print(chk(n[0]))
    t-=1
