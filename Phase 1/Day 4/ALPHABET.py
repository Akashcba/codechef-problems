
def chk(a,s):
    for i in a :
        if i in s:
            continue
        else :
            return "No"
    return "Yes"

def main():
    s = input().split(" ")[0]
    n = int(input())
    while(n > 0):
        n-=1
        a = input().split(" ")[0]
        print(chk(a,s))

if __name__ == "__main__":
    main()
