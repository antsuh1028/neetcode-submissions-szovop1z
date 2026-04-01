class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        freq = {}

        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            maxx = max(maxx, r-l+1)
        return maxx
