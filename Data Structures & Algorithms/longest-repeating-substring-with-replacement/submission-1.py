class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}

        l = 0
        r = 0

        longest = 0

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1

            max_freq = max(freq.values())

            while (r - l + 1 - max(freq.values()) > k):
                freq[s[l]] -= 1
                l+=1
            
            longest = max(longest, r - l + 1)
        return longest

            


            

            


