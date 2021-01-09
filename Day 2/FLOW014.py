
d = {'H':50,'C':0.7,'T':5600}

for i in range(int(input())):
    a,b,c = map(str,input().split())
    a = int(a)
    b = float(b)
    c = int(c)
    if a > d['H'] and b < d['C'] and c > d['T']:
        print(10)
    elif a > d['H'] and b < d['C']:
        print(9)
    elif b < d['C'] and c > d['T']:
        print(8)
    elif a > d['H'] and c > d['T'] :
        print(7)
    elif a > d['H'] or b < d['C'] or c > d['T'] :
        print(6)
    else :
        print(5)
