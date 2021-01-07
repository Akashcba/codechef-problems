# Count the number of even and odd elements in an array
# Print out their difference

t =int(input())
n = list(map(int,input().split()))
i,j=0,0
for k in n:
    if k%2==0:
        i+=1
    else :
        j+=1
print("".join(["READY FOR BATTLE" if i > j else "NOT READY"]))
