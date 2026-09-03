from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by length so we process shorter words first
        words.sort(key=len)
        
        # dp[word] = length of longest chain ending at 'word'
        dp = {}
        
        def isPredecessor(shorter, longer):
            """Check if shorter is a predecessor of longer"""
            if len(longer) != len(shorter) + 1:
                return False
            
            i, j = 0, 0
            diff_found = False
            
            # Two-pointer approach to find which char was inserted
            while i < len(shorter) and j < len(longer):
                if shorter[i] == longer[j]:
                    i += 1
                    j += 1
                else:
                    if diff_found:
                        return False
                    diff_found = True
                    j += 1
            
            return True
        
        result = 0
        
        # Process each word in order of increasing length
        for word in words:
            dp[word] = 1  # Minimum chain length is 1 (the word itself)
            
            # Try removing one character to find predecessors
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]  # Remove one character
                
                # If prev exists in our DP and forms valid chain
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
            
            result = max(result, dp[word])
        
        return result