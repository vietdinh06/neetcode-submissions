class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #What if for ech word, i split all the characters and put
        #it into a hash table. then, for each word, i will
        #see if each letter corresponds to a char in the hash

        words = {}

        for word in strs:
            alphabet = [0] * 26

            for character in word:
                alphabet[ord(character) - ord('a')] += 1

            tupleized = tuple(alphabet)
            
            if tupleized in words:
                words[tupleized].append(word)
            else:
                words[tupleized] = [word]

            
        return list(words.values())