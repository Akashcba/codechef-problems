dp = {0:0,1:1}


def sum(d,n):
    if d == 0:
        return n ## No need to Process n
    else :       ## Return n alone only as sum(0,n) = n
        global dp
        if n in dp:
            return sum(d-1,dp[n])
        else :
            dp[n] = n * (n+1)//2
        if d > 1:
            return sum(d-1,dp[n])
        else :
            return dp[n]

def main():
    t =int(input())
    while(t>0):
        t-=1
        d,n=map(int,input().split())
        print(sum(d,n))

if __name__ == "__main__":
    main()
