class Solution:
    def sortPeople(self, names, heights):
        n = len(heights)
        for i in range(n):
            for j in range(i+1, n):
                if heights[i] < heights[j]:
                    small = heights[i]
                    heights[i], heights[j] = heights[j], heights[i]
                    names[i], names[j] = names[j], names[i]       
        return names
