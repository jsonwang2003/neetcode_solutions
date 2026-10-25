class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            m = (l + r) // 2
            total = 0
            for bananas in piles:
                total += math.ceil(bananas / m)
            
            if total > h:
                l = m + 1
            else:
                r = m

        return l
            
