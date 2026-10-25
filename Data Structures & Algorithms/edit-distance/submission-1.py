class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [([0] * (len(word1) + 1)) for _ in range(len(word2) + 1)]

        # base cases
        for row in range(1, len(dp)):
            dp[row][0] = dp[row - 1][0] + 1

        for col in range(1, len(dp[0])):
            dp[0][col] = dp[0][col - 1] + 1

        # for loop with rules
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                j = col - 1
                i = row - 1

                if word1[j] == word2[i]:
                    dp[row][col] = min(
                        1 + dp[row-1][col],
                        1 + dp[row][col - 1],
                        dp[row-1][col-1]
                    )
                else:
                    dp[row][col] = 1 + min(
                        dp[row-1][col],
                        dp[row][col-1],
                        dp[row-1][col-1]
                    )

        print(dp)
        return dp[-1][-1]