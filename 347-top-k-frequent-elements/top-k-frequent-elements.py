class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        sorted_keys = sorted(count, key=count.get, reverse=True)
        i = 0
        for v in sorted_keys:
            if len(res) < k:
                res.append(v)
            else:
                break
        return res
        

            


