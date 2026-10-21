class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_1 = {}
        hash_map_2 = {}
        for c in s:
            if c in hash_map_1:
                hash_map_1[c] += 1
            else:
                hash_map_1[c] = 1

        for c in t:
            if c in hash_map_2:
                hash_map_2[c] += 1
            else:
                hash_map_2[c] = 1
        

        return hash_map_1 == hash_map_2