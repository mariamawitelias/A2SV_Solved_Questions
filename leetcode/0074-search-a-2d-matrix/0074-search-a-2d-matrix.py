class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                arr.append(matrix[r][c])
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r)//2
            if arr[mid] > target:
                r = mid - 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                return True
        return False

