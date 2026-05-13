class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lis = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                lis.append(matrix[r][c])
        heapify(lis)
        return  heapq.nsmallest(k, lis)[-1]