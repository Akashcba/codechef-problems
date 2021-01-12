# n coins can be exchanged with -> n/2 , n/3 , n/4 coins
# given n coins find max dollars we can get for it .

arr = dict()

def coins(n):
    if n < 10:
        return n
    global arr
    if n in arr:  ## if arr[n] doesn't work in case of dictionaries.
        return arr[n]
    x = coins(n//2)+coins(n//3)+coins(n//4)
    arr[n] = max(n,x)
    return arr[n]
def main():
    while True:
        try:
            n = int(input())
            print(coins(n))
        except:
            return 0

if __name__ == "__main__":
    main()
