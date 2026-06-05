class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)

        for start in range(n):
            match = True
            for j in range(n):
                if s[(start + j) % n] != goal[j]:
                    match = False
                    break

            if match:
                return True

        return False