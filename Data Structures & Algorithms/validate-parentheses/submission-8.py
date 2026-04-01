class Solution:
    def isValid(self, s: str) -> bool:
        print(len(s))
        if not s or len(s) % 2 != 0:
            return False


        dct = {"(":")",
            "{":"}",
            "[":"]"}
        stack = []
        
        for par in s:
            if par in dct.keys():
                stack.append(par)
            else:
                if not stack or dct[stack.pop()] != par:
                    return False

        return False if stack else True

        for i in range(0,len(s)//2):
            stack.append(s[i])

        for i in range(len(s)//2,len(s)):
            if dct[stack.pop()] != s[i]:
                return False
        return True

