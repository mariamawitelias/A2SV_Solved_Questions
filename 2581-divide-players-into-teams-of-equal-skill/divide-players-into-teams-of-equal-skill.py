class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill)-1
        tot = skill[0] + skill[-1]
        ans = 1
        res = 0
        while i < j:
            if skill[i] + skill[j] == tot:
                ans = skill[j] * skill[i]
                res += ans
                i += 1
                j -= 1
            else:
                return -1
        return res



