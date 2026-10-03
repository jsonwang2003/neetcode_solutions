from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_count.keys())[:k]

        