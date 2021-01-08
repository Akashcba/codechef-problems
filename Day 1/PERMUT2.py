# Check if the sequence of integers is an inverse permutation or not.
# Inverse permutation is when a[i] == a[a[i]]
t = int(input())
while (t != 0):
    n = list(map(int,input().split()))
    flag = 1
    for i in range(t):
        if i != n[n[i] - 1] - 1 :
            print("not ambiguous")
            flag = 0
            break
    if flag:
        print("ambiguous")
    t = int(input())
