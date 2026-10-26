class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, res = [1 for _ in range(len(nums))], [1 for _ in range(len(nums))], []

        prefix[0] = nums[0]
        postfix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for j in range(len(nums) - 2, -1, -1):
            postfix[j] = postfix[j + 1] * nums[j]

        for k in range(len(nums)):
            if k == 0:
                res.append(postfix[k+1])
            elif k == len(nums) - 1:
                res.append(prefix[k - 1])
            else:
                res.append(prefix[k-1] * postfix[k+1])

        return res