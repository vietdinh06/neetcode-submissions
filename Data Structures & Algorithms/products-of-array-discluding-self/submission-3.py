class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        prefix.append(1)
        prod = 1

        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            prefix.append(prod)


        suffix = [1] * len(nums)
        prod = 1
        for i in range (len(nums)-2, -1, -1):
            prod *= nums[i + 1]
            suffix[i] = prod
        output = []
        for i in range(len(nums)):
            output.append( prefix[i] * suffix[i])

        return output