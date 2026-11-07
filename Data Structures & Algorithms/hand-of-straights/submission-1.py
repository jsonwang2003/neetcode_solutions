class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = defaultdict(int)

        for num in hand:
            counts[num] += 1

        sorted_counts = dict(sorted(counts.items()))

        for key in sorted_counts.keys():
            c = sorted_counts[key]

            if c < 0:
                return False
            if c == 0:
                continue
            
            for i in range(groupSize):
                if key + i not in sorted_counts.keys():
                    return False
                sorted_counts[key + i] -= c
            
        return True
        
