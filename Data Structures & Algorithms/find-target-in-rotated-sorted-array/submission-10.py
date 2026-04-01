class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l + r)//2
            num = nums[mid]
            print(nums[l], nums[mid], nums[r])

            if num == target:
                return mid
            if nums[l] <= num:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target >= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return -1


        #     elif num > target:
        #         print("here")
        #         # print(nums[l], num, nums[mid])
        #         if nums[l] < num and nums[l] <= target <= nums[mid]:
        #             r = mid -1
                    
        #         else:
        #             print("h")
        #             l = mid + 1
        #     else:
                
        #         if nums[r] > num and nums[r] >= target >= nums[mid]:
        #             l = mid + 1
        #         else:
        #             r = mid -1
        # return -1