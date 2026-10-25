class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                # num is first in sequence
                distance = 1
                while num + 1 in numSet:
                    num += 1
                    distance += 1
                longest = max(longest, distance)

        return longest
                
