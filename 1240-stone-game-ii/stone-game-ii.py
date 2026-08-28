class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            best_result = float('-inf')

            for X in range(1, min(2 * M, n - i) + 1):

                opponent_gets = dp(i + X, max(M, X))

                my_gets = suffix_sum[i] - opponent_gets

                best_result = max(best_result, my_gets)

            memo[(i, M)] = best_result
            return best_result

        return dp(0, 1)