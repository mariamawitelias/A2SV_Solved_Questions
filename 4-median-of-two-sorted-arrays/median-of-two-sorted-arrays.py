class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                num.append(nums1[i])
                i += 1
            else:
                num.append(nums2[j])
                j += 1
        if i != len(nums1):
            num.extend(nums1[i:])
        elif j != len(nums2):
            num.extend(nums2[j:])
        print(num)
        r = len(num)
        if len(num) % 2 == 1:
            mid = r // 2
            return float(num[mid])
        else:
            mid1 = num[r // 2]
            mid2 = num[r // 2 - 1]
            return (float(mid1) + float(mid2)) / 2.0
            
        
        
        