class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        path = []
        def backtrack(idx):
            if idx == len(num):
                if len(path) >= 3:
                    return True
                return False
            
            for i in range(idx, len(num)):
                if len(path) < 2 or int(num[idx:i + 1]) == path[-1] + path[-2]:
                    path.append(int(num[idx:i + 1]))
                    if backtrack(i + 1): return True
                    path.pop()
                if num[idx] == "0": return False
            return False

        return backtrack(0)