import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        heapq.heapify(arr)

        for num in nums:
            heapq.heappush(arr, num)
            if len(arr) > k:
                heapq.heappop(arr)
        return arr[0]