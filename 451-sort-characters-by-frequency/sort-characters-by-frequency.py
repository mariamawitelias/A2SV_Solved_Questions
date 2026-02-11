class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_keys = sorted(count, key=count.get, reverse=True)
        res = ""
        for key in sorted_keys:
            for i in range(count[key]):
                res += key
        return res

        