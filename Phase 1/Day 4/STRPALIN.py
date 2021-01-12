

def main():
    t = int(input())
    while(t>0):
        t-=1
        a =input().split(" ")[0]
        b = input().split(" ")[0]
        res = [x for x in a if x in b]
        if len(res):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
