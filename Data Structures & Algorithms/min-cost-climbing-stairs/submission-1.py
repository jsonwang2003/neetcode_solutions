class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        A = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            A[i] = min(A[i-1] + cost[i-1], A[i-2] + cost[i-2])
        
        return A[-1]