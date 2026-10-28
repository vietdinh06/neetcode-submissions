class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        c = 0

        result = []

        while (c < len(nums) - 2):
            a = c + 1
            b = len(nums) - 1

            while (a < b):
                t = nums[a] + nums[b] + nums[c]


                if t > 0:
                    b-=1

                if t < 0:
                    a+=1

                if t == 0:
                    result.append([nums[a], nums[b], nums[c]])

                    a+=1
                    b-=1
                
                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                
            c+=1
            while c < len(nums) - 2 and nums[c] == nums[c - 1]:
                c += 1


        return result
