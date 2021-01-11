# Estimate the difference b/w the two strings.
# Store points where s1[i] == s2[i]
# minimal = total unequal stored values
# maximum = minimal + total_unequal_'?' + equal_'?'
def sum(a,b):
    if len(a) != len(b): return 0 ;
    ls = [0,0,0] # [q, total, temp]
    for i in range(len(a)):
        if a[i] == '?' and b[i] == '?': ls[0] +=1 ;
        elif a[i] == '?' or b[i] == '?' : ls[1] += 1 ;
        elif a[i] != b[i] : ls[2] += 1 ;
    return str(ls[2]) + (" ")+str(ls[0] + ls[1] + ls[2])

def main():
    t = int(input())
    while(t>0):
        t-=1
        s1 = input().split(" ")[0]
        s2 = input().split(" ")[0]
        print(sum(s1,s2))

if __name__ == '__main__' :
    main()
