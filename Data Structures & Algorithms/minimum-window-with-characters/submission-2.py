class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}

        for c in t:
            if c in freq_t:
                freq_t[c] += 1
            else:
                freq_t[c] = 1

        valid = len(t)
        sub_len = float('inf')
        l = 0

        min_l = 0
        min_r = 0

        for r in range(len(s)):
            if s[r] in freq_t:         
                if freq_t[s[r]] > 0:
                    valid -= 1
                freq_t[s[r]] -= 1

            while valid == 0:
                if sub_len > r - l + 1:
                    sub_len = r - l + 1
                    min_r = r
                    min_l = l

                if s[l] in freq_t:
                    freq_t[s[l]] += 1
                    if freq_t[s[l]] > 0:
                        valid += 1
                l += 1     
        
        if sub_len == float('inf'):
            return ""

        return s[min_l:min_r + 1]     

            
