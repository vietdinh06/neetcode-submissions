class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}

        for c in t:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1

        valid = False
        sub_len = float('inf')
        l = 0
        r = 0

        min_l = 0
        min_r = 0

        while r < len(s):
            if s[r] in freq_t:
                freq_t[s[r]] -= 1
            
            valid = all(value <= 0 for value in freq_t.values())

            while valid:
                if sub_len > r - l + 1:
                    sub_len = r - l + 1
                    min_r = r
                    min_l = l

                if s[l] in freq_t:
                    freq_t[s[l]] += 1
                valid = all(value <= 0 for value in freq_t.values())
                l += 1     

            r += 1  
        
        if sub_len == float('inf'):
            return ""

        return s[min_l:min_r + 1]     

            
