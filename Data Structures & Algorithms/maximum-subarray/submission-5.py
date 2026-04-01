class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        currSum = 0 #2 -1->0 4 2 4 3 7

        for num in nums:
            currSum = max(0, currSum) + num
            maxSum = max(maxSum, currSum)


        return maxSum