class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        letters = set()
        longest = 0

        for i in range(len(s)):
            print(s[l:r])
            if s[i] in letters:
                print("in set")
                while s[i] in letters:
                    letters.remove(s[l])
                    print(letters)
                    
                    l+=1
                    
            letters.add(s[i])
            longest = max(longest, r-l)
            r+=1
            
            print(longest)
            # print(letters)
            

        return longest