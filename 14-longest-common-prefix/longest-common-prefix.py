class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=strs[0]  
        for strr in strs[1:]:
            j=0
            while j<len(pref) and j<len(strr) and pref[j]==strr[j]:
                j+=1
            pref=pref[:j]
            if not pref:
                return ""
        return pref
        

        
        