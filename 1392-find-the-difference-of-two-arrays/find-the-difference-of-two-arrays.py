class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # num3 = set(nums1 + nums2)
        # ans1 = []
        # ans2 = []
        # for i in num3:
        #     if i in nums1 and i not in nums2:
        #         ans1.append(i)
        #     elif i in nums2 and i not in nums1:
        #         ans2.append(i)
        # return [ans1, ans2]
        table = defaultdict(list)
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans1, ans2 = [], []
        for i in nums1:
            table[i].append(1)
        for i in nums2:
            table[i].append(2)
        for k, v in table.items():
            if len(v) == 1:
                if v[0] == 1:
                    ans1.append(k)
                else:
                    ans2.append(k)
        return [ans1, ans2]


        