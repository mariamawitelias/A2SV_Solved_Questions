class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            l = []
            for j in range(len(image[0])-1, -1, -1):
                if image[i][j] == 0:
                    l.append(1)
                else:
                    l.append(0)
            res.append(l)
        return res
                

        