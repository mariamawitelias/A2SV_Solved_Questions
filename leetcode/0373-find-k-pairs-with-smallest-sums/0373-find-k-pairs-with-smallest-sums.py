class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        res = []
        heap = []
        for i in range(min(m, k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(res) < k:
            curr_sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return res