class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            left,right = nums[:i], nums[i+1:]

            product = 1
            for num in left:
                product *= num
            for num in right:
                product *= num
            final.append(product)

        return final