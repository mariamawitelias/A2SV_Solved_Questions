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
    n, k = numbers()
    a = numbers()
    gaps = []
    for i in range(n-1):
        gaps.append(a[i+1]-a[i])
    gaps.sort(reverse = True)
    cost = 0
    for i in range(k-1):
        cost += gaps[i]
    initial = a[-1] - a[0]
    print(initial - cost)
  
    return

for _ in range(test_cases(1)):
    solve()
