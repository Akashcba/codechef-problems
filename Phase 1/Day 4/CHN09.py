def chk(a):
    ls = [0,0]
    for i in a :
        if i == 'a':
            ls[0]+=1
        else:
            ls[1]+=1
    return min(ls)


def main():
    t =int(input())
    while(t>0):
        t-=1
        s = input().split(" ")[0]
        print(chk(s))


if __name__ == "__main__":
    main()
