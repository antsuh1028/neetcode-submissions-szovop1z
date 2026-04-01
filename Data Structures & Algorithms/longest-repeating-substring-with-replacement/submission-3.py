class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,1
        alpha = [0] * 26
        result = 0

        for letter in s:
            print(ord(letter), ord('A'))
            curr_letter = ord(letter) - ord('A')
            print(curr_letter)
            alpha[curr_letter] += 1
            print(alpha)

            diff = (r-l) - max(alpha)
            while diff > k:
                
                alpha[ord(s[l]) - ord('A')] -= 1
                l += 1
                diff = (r-l) - max(alpha)
            print(alpha)

            result = max(result, r-l)
            r+=1
        return result