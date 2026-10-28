class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        list_s = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                list_s.append(s[i])
                continue
            
            if len(list_s) == 0:
                return False

            if s[i] == ")":
                if list_s[-1] == "(":
                    list_s.pop()
                else:
                    return False
            if s[i] == "}":
                if list_s[-1] == "{":
                    list_s.pop()
                else:
                    return False

            if s[i] == "]":
                if list_s[-1] == "[":
                    list_s.pop()
                else:
                    return False

        return len(list_s) == 0
        
        
