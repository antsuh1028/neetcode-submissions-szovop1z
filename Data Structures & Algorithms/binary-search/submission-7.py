class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)
        

        while l < r:
            # print(nums[l:r+1])
            mid = (r+l)//2
            num = nums[mid]
            # print(num)
            if num == target:
                return mid
            elif num < target:
                l = mid +1
            else:
                r = mid
        return -1



