class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lett = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []
        def backtrack(i, comb):
            if i == len(digits):
                res.append(comb[:])
                return
            for v in lett[digits[i]]:
                backtrack(i+1, comb+v)
        backtrack(0, "")
        return res


