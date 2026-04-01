class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_size = 0
        st = set()

        for r in range(0,len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            print(l,r)
            max_size = max(max_size, len(s[l:r+1]))
        return max_size