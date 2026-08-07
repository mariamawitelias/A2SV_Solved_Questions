class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        res = num_people * [0]
        count = 0
        j = 0
    
        while candies > 0:
            if j == num_people:
                j = 0
            if candies > count:
                count += 1
                res[j] += count
                j+=1
                candies -= count
            else:
                res[j] += candies
                candies = 0
        return res
