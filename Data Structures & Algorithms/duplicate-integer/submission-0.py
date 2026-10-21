class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_list = set()

        for i in nums:
            if i in hash_list:
                return True
            hash_list.add(i)

        return False