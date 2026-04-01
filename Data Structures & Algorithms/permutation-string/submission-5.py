class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0] * 26
        main = [0] * 26
        for s in s1:
            main[ord(s) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            freq[ord(s2[r]) - ord('a')] += 1
            if r-l+1 > len(s1):
                freq[ord(s2[l]) - ord('a')] -= 1
                l += 1 
            if freq == main:
                return True
        return False
            


        