class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        l = 0
        write = 0

       
        while l < n:
            r = l

            while r < n and chars[r] == chars[l]:
                r += 1

            length = r - l

            chars[write] = chars[l]

            write += 1

            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1

            l = r

        return write
            