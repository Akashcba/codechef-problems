
n,t = map(int,input().split())  # Assigning 2 inputs to two vars
#print(n,t)
count = 0
while n > 0:
    ti = int(input())
    if not (ti % k):
        count += 1
    n-=1
print(count)
