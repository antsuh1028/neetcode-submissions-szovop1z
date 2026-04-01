class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # track total
        gmax = -float("inf")
        gmin = float("inf")
        lmax = -float("inf")
        lmin = float("inf")
        total = 0

        for num in nums:
            lmax = max(0,lmax) + num
            gmax = max(gmax, lmax)

            lmin = min(0,lmin) + num
            gmin = min(gmin, lmin)
        
            total += num
        print(total, gmin,gmax)
        return gmax if gmax < 0 else max(total - gmin, gmax)

        


        