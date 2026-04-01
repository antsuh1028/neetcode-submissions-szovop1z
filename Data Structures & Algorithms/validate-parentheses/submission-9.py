class Solution:
    def isValid(self, s: str) -> bool:

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

        return not stack
