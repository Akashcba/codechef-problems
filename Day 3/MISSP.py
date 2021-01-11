



def main():
    t =int(input())
    while(t>0):
        t-=1
        dp = dict()
        ls=[]
        for i in range(int(input())):
            a = int(input())
            if a in dp :
                dp[a]+=1
            else :
                dp[a] = 1
        for k,v in dp.items():
            if v%2 != 0:
                print(k,sep=' ')


if __name__ == '__main__':
    main()
