class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ababd

        # "center" so abAbd
        # take the left, bA
        # take the right, bAb

        # the ends are the same. this is a palindrome, so return

        # abbc

        # "center", so abBc
        # take the left, bb

        # the ends are the same. this is a palindrome, so return

        res = ""

        longest = 0

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    res = s[l:r+1]
                    longest = r - l + 1
                
                r += 1
                l -= 1

            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    res = s[l:r+1]
                    longest = r - l + 1
                
                r += 1
                l -= 1

        return res