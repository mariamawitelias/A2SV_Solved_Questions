class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        r, c = 0, 0
        for _ in range(len(mat) * len(mat[0])):
            res.append(mat[r][c])
            if (r + c) % 2 == 0:
                if c == len(mat[0])-1:
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == len(mat)-1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return res



        