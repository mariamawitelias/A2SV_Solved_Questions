class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            found = False
            for start, end in ranges:
                if i >= start and i <= end:
                    found = True
                    break
            if not found:
                return False
        return True


