class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#" + strs[i]

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        num = 0

        while num < len(s):
            pound = num

            while s[pound] != '#':
                pound += 1

            length = int(s[num:pound])

            decoded.append(s[pound + 1 : pound + 1 + length])

            num = pound + 1 + length

        return decoded