# Program to find Factorial value of a number entered by the user.

def fact(i):
    if i<=1:
        return 1
    else :
        return i*fact(i-1)
t = int(input())
while t--:
    n = int(input())
    print(fact(n))
# Codechef ide requires you to
# give custom input in oredr to submit
# problems in python 3
