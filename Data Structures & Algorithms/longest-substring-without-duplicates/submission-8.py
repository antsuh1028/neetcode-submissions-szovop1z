class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx = 0
        dct = {}

        for r in range(len(s)):
            if s[r] in dct and dct[s[r]] >= l:
                l = dct[s[r]] + 1
            dct[s[r]] = r
            mx = max(mx, r-l+1)
        return mx
