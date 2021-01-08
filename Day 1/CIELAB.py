def L(a):
  return(int(a))

a,b = map(L,input().split())
ans = a - b
if ans%10:
    print(''.join([str(ans - 1) if ans > 1 else str(2) ]))
# Taking account a-b =1 because 1 -1 = 0
# And 0 is not the accepted answer .
else:
    print(ans + 1)
#print("a - b is",a-b)
#print(ans)
