# Find the sum of Smallest and Second Smallest elements
# in an array
# Brute way : Sort O(nlogn)
# Traverse Twice : O(n)
# Traverse only once using two variables.
import sys
# Sys contains the maxint value that an integer can take
def sum(ls=[1,2,3,4,5]):
    first = second = sys.maxsize
# sys.maxint deprecated in python 3
    for i in ls:
         if i < first :
             second = first
             first = i
         elif i < second:
             second = i
    return first + second
t = int(input())
while(t>0):
    n = int(input())#Temporary var denoting size of input()
    inp = list(map(int,input().split()))
    print(sum(inp))
    t-=1
