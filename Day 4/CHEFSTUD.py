def chk(s):
    result = 0
    for i in range(len(s) - 1):
        if s[i] == '<' and s[i+1] == '>':
            result+=1
    return result

def main():
    t = int(input())
    while(t>0):
        t-=1
        s = input().split(" ")[0]
        print(chk(s))

if __name__ == '__main__':
    main()
