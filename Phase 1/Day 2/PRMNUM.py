# Using Modified Sieve Of Erasthones to print the Nth Prime Number

N = 1299711  # Value of N set to meet the boundary condition.
smallest_factor = [0]*(N+1)
prime = []
def modified_sieve():
    global prime, smallest_factor, N
    for i in range(2,N+1):
        if smallest_factor[i] == 0 : # Its a prime number
            smallest_factor[i] = i
            prime.append(i)
        # If not prime and cut all its factors
        j = 0
        while(j<len(prime) and prime[j]<=smallest_factor[i] and i*prime[j]<= N):
            smallest_factor[i*prime[j]] = prime[j]
            j+=1

modified_sieve()
for i in range(int(input())):
    n = int(input())
    print(prime[n - 1 ])
