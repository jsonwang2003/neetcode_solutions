class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        total, maxL, maxR = 0, 0, 0

        while l < r:            
            if height[l] > maxL:
                maxL = height[l]
            if height[r] > maxR:
                maxR = height[r]
            
            if maxL < maxR:
                total += maxL - height[l]
                l += 1
            else:
                total += maxR - height[r]
                r -= 1
            
        return total