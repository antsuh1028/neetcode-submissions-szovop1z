class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)
        l = 0
        
        

        while l < r:
            print(l,r)
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid +1
        return -1



