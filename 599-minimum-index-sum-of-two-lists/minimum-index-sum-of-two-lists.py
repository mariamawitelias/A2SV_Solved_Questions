class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        table = defaultdict(list)
        res = []
        ans = []
        for i, word in enumerate(list1):
            if word in list2:
                j = list2.index(word)
                table[i + j].append(word)
                ans.append(i + j)
        x = min(ans)
        for key, value in table.items():
            if key == x:
                res = value
        return res
        

        