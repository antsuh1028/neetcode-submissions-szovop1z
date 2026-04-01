class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        mx = -float("inf")
        curr = 0

        for n in nums:
            curr = max(0, curr) + n
            mx = max(mx, curr)

        return mx
