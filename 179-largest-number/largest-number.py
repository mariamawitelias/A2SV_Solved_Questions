class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = []
        res = ""
        for i in nums:
            a.append(str(i))
        a.sort(key=cmp_to_key(
            lambda a, b: -1 if a+b > b+a else (1 if a+b < b+a else 0)
        ))
        for i in range(len(a)):
            res += a[i]
        return "0" if res[0] == "0" else res
        