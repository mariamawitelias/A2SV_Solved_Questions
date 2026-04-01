class Solution:
    def splitString(self, s: str) -> bool:
    
        
        def backtrack(i, sub):
            if i == len(s):
                if sub == s:
                    return False
                return True
            next = ""
            for j in range(i, len(s)):
                next += s[j]

                if sub == "" or int(sub) - int(next) == 1:
                    if backtrack(j+1, next):
                        return True
            return False
        return backtrack(0, "") 
            

