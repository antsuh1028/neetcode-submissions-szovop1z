class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n) solution
        # first, second = 0,1

        # while second < len(nums) and nums[first] < nums[second]:
        #     print(first,second)
        #     first += 1
        #     second += 1
        
        # return nums[second] if second < len(nums) else nums[0]

        l,r = 0, len(nums)-1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                # return nums[mid]
                l = mid + 1
            else:
                r = mid
        return nums[l]

            # print(nums[l], nums[r], nums[mid])
            # if nums[l] < nums[r]:
            #     return nums[l]
            # if nums[l] > nums[mid] < nums[r]:
            #     return nums[mid]
            # if nums[mid] > nums[l] :
            #     l = mid +1
            # else:
            #     r = mid -1
        return nums[mid]

        