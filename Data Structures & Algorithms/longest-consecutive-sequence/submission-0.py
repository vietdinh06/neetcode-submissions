class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums.sort()

        max_cons = 1
        cons = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cons += 1

            elif nums[i] - nums[i-1] != 0:
                max_cons = max(max_cons, cons)
                cons = 1

        max_cons = max(max_cons, cons)
        cons = 1

        return max_cons

    