class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Make hash table with our numbers
        A = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff not in A:
                A[n] = i
            else:
                return [A[diff], i]
        return []

