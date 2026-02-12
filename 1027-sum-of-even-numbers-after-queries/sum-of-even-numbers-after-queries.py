class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        totalEvenNumSum = sum([num  for num in nums if num % 2 == 0])
        result = []
        for val, idx in queries:
            oldVal = nums[idx]
            nums[idx] += val  
            if oldVal % 2 == 0:
                totalEvenNumSum -= oldVal
            
            if nums[idx] % 2 == 0:
                totalEvenNumSum += nums[idx]
                
        
            result.append(totalEvenNumSum)            
        
        return result
            
                