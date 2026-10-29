class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashed_set = set()

        l = 0

        longest = 0
        for r in range(len(s)):
            while s[r] in hashed_set:
                hashed_set.remove(s[l])
                l += 1
                
            hashed_set.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


            

