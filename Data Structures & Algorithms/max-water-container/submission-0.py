class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        area = 0
        
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            temp_area = width * height
            area = max(area, temp_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return area