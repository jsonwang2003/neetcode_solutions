class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        max_heap = [[value, key] for key, value in count.items()]
        heapq.heapify_max(max_heap)

        result = []
        while len(result) < k:
            result.append(heapq.heappop_max(max_heap)[1])

        return result