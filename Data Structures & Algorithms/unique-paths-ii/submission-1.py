class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1

        if obstacle[-1][-1] == 1:
            return 0

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if row == m-1 and col == n-1:
                    # at bottom right
                    continue
                
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                elif row == m-1:
                    dp[row][col] = dp[row][col + 1]
                elif col == n-1:
                    dp[row][col] = dp[row + 1][col]
                else:
                    dp[row][col] = dp[row + 1][col] + dp[row][col + 1]

        return dp[0][0]

