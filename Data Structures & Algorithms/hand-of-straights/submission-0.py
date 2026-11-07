class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = defaultdict(int)

        for num in hand:
            counts[num] += 1

        for key in counts:
            c = counts[key]

            if c < 0:
                return False
            if c == 0:
                continue
            
            for i in range(groupSize):
                counts[key + i] -= c
            
        return True
        
