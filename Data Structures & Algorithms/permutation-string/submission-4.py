class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,r = 0, len(s1)
        string = sorted(s1)
        print(string)
        print(len(s2))
        while r <= len(s2):
            print(r)
            new_string = s2[l:r]
            print(new_string)
            if sorted(new_string) == string:
                return True
            l+=1
            r+=1


        return False