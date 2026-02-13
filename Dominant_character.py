from math import ceil, sqrt, log, log2, pow, floor, gcd, inf, isqrt, lcm
import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint

number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
prefix_sum = lambda arr: list(itertools.accumulate(arr))

def solve():
    n = number()
    s = word()
    ans = float('inf')
    for i in range(n):
        f = [0, 0, 0]   
        f[ord(s[i]) - ord('a')] += 1
        for j in range(i + 1, min(n, i + 7)):
            f[ord(s[j]) - ord('a')] += 1

            if f[0] > f[1] and f[0] > f[2]:
                ans = min(ans, j - i + 1)

    if ans == float('inf'):
        ans = -1
    print(ans)
    
    return

for _ in range(test_cases()):
    solve()
