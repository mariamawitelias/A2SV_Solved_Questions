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
    n, l, r = numbers()
    sock = numbers()
    res = 0
    left = Counter(sock[:l])
    right = Counter(sock[l:])
    for c in left:
        if c in right:
            tmp = min(left[c], right[c])
            left[c] -= tmp
            right[c] -= tmp
    for c in right:
        if c in left:
            tmp = min(left[c], right[c])
            left[c] -= tmp
            right[c] -= tmp
    L = sum(left.values())
    R = sum(right.values())
    if L < R:
        left, right = right, left
        L, R = R, L
    diff = L - R
    res += R
    for c in left:
        if diff <= 0:
            break
        use = min(left[c]//2, diff//2)
        res += use
        diff -= use * 2
    res += diff
    print(res)
    return

for _ in range(test_cases()):
    solve()
