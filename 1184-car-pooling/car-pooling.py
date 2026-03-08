class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        freq = [0]*1002
        i=0
        l = len(trips)
        while i < l:
            freq[trips[i][1]] += trips[i][0]
            freq[trips[i][2]]-= trips[i][0]
            i+=1
        
        pref = 0
        i=0
        while i<1002:
            pref+=freq[i]
            if pref > capacity:
                return False
            i+=1
        
        return True