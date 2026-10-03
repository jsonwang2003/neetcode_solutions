class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        A = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            A.append(cost[i] + min(A[i-1], A[i-2]))
        
        return min(A[-1], A[-2])