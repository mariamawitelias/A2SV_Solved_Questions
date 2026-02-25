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
    s = word()
    t = word()
    cs = Counter(s)
    ct = Counter(t)
    for c in cs:
        if cs[c] > ct[c]:
            print("Impossible")
            return
    left = []
    for ch in sorted(ct.keys()):
        left.extend([ch] * (ct[ch] - cs[ch]))
    l = "".join(left)
    res = []
    i = 0
    for ch in l:
        while i < len(s) and s[i] <= ch:
            res.append(s[i])
            i += 1
        res.append(ch)
    while i < len(s):
        res.append(s[i])
        i += 1
    print("".join(res))
for _ in range(test_cases()):
    solve()
