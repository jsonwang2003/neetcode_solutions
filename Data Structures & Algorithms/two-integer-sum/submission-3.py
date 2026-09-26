class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        goals = {}

        for i in range(len(nums)):
            if nums[i] in goals.keys():
                return [goals[nums[i]], i]
            goals[target - nums[i]] = i

         