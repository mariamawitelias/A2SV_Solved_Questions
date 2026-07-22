class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        y = []
        for i in range(left, right + 1):
            x = list(str(i))
            if "0" not in x:
                ok = True
                for j in range(len(x)):
                    if i % int(x[j]) != 0:
                        ok = False
                        break
                if ok:
                    y.append(i)
        return y