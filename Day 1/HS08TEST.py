n = list(map(float,input().split()))
if n[0] % 5 == 0:
    ans = n[1] - n[0] - 0.5000
    print(''.join([str(ans) if ans > 0 else str(n[1]) ]))
else :
    print(n[1])


# Use
# print( "{0:.2f}".format(a)) --> For precision upto 2 digits
# after the decimal point
