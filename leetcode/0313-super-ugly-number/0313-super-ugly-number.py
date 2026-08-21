class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        k = len(primes)

        ptr = [0] * k
        next = list(primes)

        for i in range(1, n):
            next_ugly = min(next)
            ugly[i] = next_ugly

            for j in range(k):
                if next[j] == next_ugly:
                    ptr[j] += 1
                    next[j] = primes[j] * ugly[ptr[j]]
        return ugly[n - 1]