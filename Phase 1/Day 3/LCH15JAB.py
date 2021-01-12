
def chk(a,dp):
    for i in a :
        if i in dp :
            dp[i]+=1
        else :
            dp[i] = 1
    sum = 0
    for i in dp.values():
        sum += i
    for i in dp.keys():
        if dp[i] == sum - dp[i]:
            return "YES"
    return "NO"


def main():
    t = int(input())
    while(t>0):
        t-=1
        s = input().split(" ")[0]
        dp = dict()
        print(chk(s,dp))


if __name__ == '__main__':
    main()
