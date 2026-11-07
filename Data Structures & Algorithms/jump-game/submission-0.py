class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            dp[i] = (True in dp[i: i + nums[i] + 1])

        return dp[0]
