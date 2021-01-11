dp = []
dp[1] = 1
dp[0] = 0
def sum(d,n):
    for i in range(d):
        if n in dp:
            return dp[n]
        else :
            x = n + sum(d-1,n-1)
            dp[n] = x
            return dp[n]

t =int(input())
while(t>0):
    t-=1
