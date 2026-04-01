class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        mx = 0
        dct = {}
        st = set()

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])

            mx = max(mx, r-l+1)
        return mx
