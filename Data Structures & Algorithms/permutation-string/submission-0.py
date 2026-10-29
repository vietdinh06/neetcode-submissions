class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}

        for c in s1:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        l = 0

        for r in range(len(s2)):
            if s2[r] in freq:
                freq[s2[r]] -= 1

                while freq[s2[r]] < 0:
                    freq[s2[l]] += 1
                    l+=1
            else:
                while (l <= r):

                    if s2[l] in freq:
                        freq[s2[l]] += 1

                    l += 1
            
            if r - l + 1 == len(s1):
                return True

        return False
        