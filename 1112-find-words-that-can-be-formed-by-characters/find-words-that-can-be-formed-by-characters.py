class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch = Counter(chars)
        res = 0
        for word in words:
            c = ch.copy()
            for j in word:
                if j in c and c[j] != 0:
                    c[j] -= 1
                else:
                    res -= len(word)
                    break
            res += len(word)

        return res
        
