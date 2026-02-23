class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        length = int(math.sqrt(c))
        i, j = 0, length
        while i <= j:
            if (i * i) + (j * j) > c:
                j -= 1
            elif (i * i) + (j * j) < c:
                i -= 1
            else:
                return True
        return False

        


        