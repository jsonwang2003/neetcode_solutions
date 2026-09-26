class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        goals = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in goals.keys():
                return [goals[num], i]
            goals[target - num] = i

         