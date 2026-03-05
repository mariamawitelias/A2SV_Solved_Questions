class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.pre = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.pre[r][c] = matrix[r][c] + self.pre[r-1][c] + self.pre[r][c-1] - self.pre[r-1][c-1]
   
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.pre[row2][col2] - self.pre[row2][col1-1] - self.pre[row1-1][col2] + self.pre[row1-1][col1-1]
       


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)