class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_t = Counter(t)
        count_s = Counter(s)
        minn = 0
        for k, v in count_s.items():
            if k in count_t:
                if v == count_t[k]:
                    minn += v
                else:
                    minn += min(v, count_t[k])
        return len(s) - minn 


        