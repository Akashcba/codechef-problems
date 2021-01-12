# Trainling Zeros of a factorial
# is an infinite sum of
# n /5 + n/5^2 +n/5^3 .....

def f(a):
    ans = 0
    while(a>0):
        ans += a // 5
        a = a//5
    return ans


t = int(input())
while(t>0):
    t-=1
    n = int(input())
    print(f(n))
