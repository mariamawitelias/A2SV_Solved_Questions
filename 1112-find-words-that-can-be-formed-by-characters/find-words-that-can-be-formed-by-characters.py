class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        # ans = []
        # for i in words:
        #     j = 0
        #     while j < len:
        #         if i[j] not in chars:
        #             break
        #         else:
        #             j += 1
        #     ans.append()
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
        