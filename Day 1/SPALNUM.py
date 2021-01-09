#S[N]:=sum of palindromic number not greater
# than N in the following way:
#S[0] = 1
#for N = 1 to 100000:
#    S[N] = S[N - 1]
#    if is_palindromic(N):
#        S[N] += N
# This is based on the same principle as
# the sieve of erasthones
# Find S[n] for the entire range
# Get the values for range [l,r]
# Using s[r+1] - s[l-1]

s =[0]*100001

def palindrome(N):
    return 1 if (str(N)[:] == str(N)[::-1])  else 0

def count():
    global s
    s[0] = 1
    for n in range(1,100001):
        s[n] = s[n-1]
        if palindrome(n):
            s[n] += n

def sum(i):
    if i < 0:
        i = 0
    return s[i]

t = int(input())
count()
while(t>0):
    t-=1
    l,r=map(int,input().split())
    print(sum(r) - sum(l-1))
#    print("Sum of r is",sum(r),"sum of l is",sum(l))
#print(s[:50])
#print(palindrome(22))
