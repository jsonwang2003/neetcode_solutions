class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                top_left = self.dp[i-1][j-1]
                top = self.dp[i-1][j]
                left = self.dp[i][j-1]
                current = matrix[i-1][j-1] # 0 based
                # dp[i][j] = dp[i-1][j] + dp[i][j-1] + matrix[i][j] - dp[i-1][j-1]
                self.dp[i][j] = current + top + left - top_left

        print(self.dp)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top_left = self.dp[row1][col1]
        top = self.dp[row1][col2+1]
        left = self.dp[row2+1][col1]
        bottom_right = self.dp[row2+1][col2+1]

        return bottom_right - top - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)