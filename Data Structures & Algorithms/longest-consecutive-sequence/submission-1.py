class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        hashed = set(nums)

        max_s = 1
        for num in hashed:
            if (num - 1 not in hashed):
                seq = 1
                start = num

                while (start + 1 in hashed):
                    seq+=1
                    start += 1

                if seq > max_s:
                    max_s = seq
        return max_s


            
                
            
        

    