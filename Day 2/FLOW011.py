# cook your dish here

for i in range(int(input())):
    sal = int(input())
    if sal < 1500:
        print(sal*(1+.10+.90))
    elif sal >= 1500:
        print(sal*(1+.98) + 500)
