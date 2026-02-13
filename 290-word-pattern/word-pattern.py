class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        if len(word) != len(pattern):
            return False
        w = set()
        table = {}
        for x, y in zip(pattern, word):
            if x in table:
                if table[x] != y:
                    return False
            else:
                if y in w:
                    return False
                table[x] = y
                w.add(y)
        return True

        
        