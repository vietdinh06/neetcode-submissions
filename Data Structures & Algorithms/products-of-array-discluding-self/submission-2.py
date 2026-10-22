class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        pre = [1] * len(nums)
        output = []

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]


        for i in range(len(nums)):
            output.append(pre[i] * suffix[i])

        return output
