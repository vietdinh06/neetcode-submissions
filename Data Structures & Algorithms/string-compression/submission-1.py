class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)

       # [ a, a, b, b]

        l = 0

        write = 0

        r = 0
        while r <= n:
            if r == n or chars[r] != chars[l]:
                length = r - l

                chars[write] = chars[l]
                write += 1

                if length > 1:
                    for digit in str(length):
                        chars[write] = digit
                        write += 1
                l = r

            r += 1

        return write




            