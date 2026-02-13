class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        for r in range(len(matrix[0])):
            ress = []
            for c in range(len(matrix)):
                ress.append(matrix[c][r])
            res.append(ress)
        return res

        
