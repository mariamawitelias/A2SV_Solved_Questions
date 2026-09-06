class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        counts = Counter(s)
        if max(counts.values()) <= k:
            return 0
        min_len = n
        left = 0
        for right, char_right in enumerate(s):
            counts[s[right]] -= 1   
            while all(v <= k for v in counts.values()):
                min_len = min(min_len, right - left + 1)
                counts[s[left]] += 1  
                left += 1               
        return min_len