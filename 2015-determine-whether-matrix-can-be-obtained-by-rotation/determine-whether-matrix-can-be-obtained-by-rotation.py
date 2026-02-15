class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            for r in range(len(mat)):
                for c in range(r, len(mat[0])):
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
            for r in range(len(mat)):
                mat[r].reverse()
            if mat == target:
                return True
        return False