class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        if nums[high] > nums[low]:
            return nums[low]

        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            else:
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid

        return nums[low]
