class Solution:
    def isSubset(self, a, b):
        from collections import Counter
        count_a = Counter(a)
        count_b = Counter(b)
        
        for x in count_b:
            if count_b[x] > count_a.get(x, 0):
                return False
                
        return True
