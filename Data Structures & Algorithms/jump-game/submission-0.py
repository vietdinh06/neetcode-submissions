class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0 


        #[1, 2, 0, 1, 0]
        # take 1. jump to index[1]
        # take 2. jump to index[3] (or index[1] + 2)
        # take 1. jump to index[4] (or index[3] + 1)
        # end