class Solution:
    def climbStairs(self, n: int) -> int:
        A = [1, 1]

        for i in range(2, n+1):
            A.append(A[i-1] + A[i-2])
        
        return A[n]