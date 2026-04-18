class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0    
        minVal = min(nums)
        maxVal = max(nums)
        if minVal == maxVal:
            return 0
        bucketSize = max(1, (maxVal - minVal) // (n - 1))
        bucketCount = (maxVal - minVal) // bucketSize + 1
        buckets = [[None, None] for _ in range(bucketCount)]
        for num in nums:
            bucket = (num - minVal) // bucketSize
            if buckets[bucket][0] is None:
                buckets[bucket][0] = num
                buckets[bucket][1] = num
            else:
                buckets[bucket][0] = min(buckets[bucket][0], num)
                buckets[bucket][1] = max(buckets[bucket][1], num)
        prevMax = None
        maxGap = 0
        for currMin, currMax in buckets:
            if currMin is None:
                continue
            if prevMax is not None:
                maxGap = max(maxGap, currMin - prevMax)
            prevMax = currMax     
        return maxGap
        