class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n) solution
        first, second = 0,1

        while second < len(nums) and nums[first] < nums[second]:
            print(first,second)
            first += 1
            second += 1
        
        return nums[second] if second < len(nums) else nums[0]
        