class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        res = []
        for r in range(len(img)):
            l = []
            for c in range(len(img[0])):
                cell = 0
                count = 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if 0 <= i < len(img) and 0 <= j < len(img[0]):
                            cell += img[i][j]
                            count += 1
                ave = cell//count
                l.append(ave)
            res.append(l)          
        return res

        