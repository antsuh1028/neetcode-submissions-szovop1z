class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        MArea = 0

        while l < r:
            area = (r-l)*min(heights[l],heights[r])
            print(r-l,heights[l],heights[r],area)
            MArea = max(area,MArea)
            # pritn(MArea)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return MArea