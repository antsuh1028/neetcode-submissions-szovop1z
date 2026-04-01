class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        dct = {"[": "]", "(":")", "{":"}"}

        stack = []
        for paren in s:
            if paren in dct.keys():
                stack.append(paren)
            if paren in dct.values():
                if len(stack) > 0:
                    if dct[stack.pop()] != paren:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
        