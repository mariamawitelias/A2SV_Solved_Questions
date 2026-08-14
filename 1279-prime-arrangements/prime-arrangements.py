class Solution:
    def numPrimeArrangements(self, n):
        M = 10**9 + 7
        # sieve
        prime = [True] * (n+1)
        prime[0] = prime[1] = False
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i, n+1, i):
                    prime[j] = False
        countPrimes = sum(prime)
        
        ans = 1
        for i in range(1, countPrimes+1):
            ans = (ans * i) % M
        for i in range(1, n - countPrimes + 1):
            ans = (ans * i) % M
        return ans