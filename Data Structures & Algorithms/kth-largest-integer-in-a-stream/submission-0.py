import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.max_size = k
        self.heap = nums
        heapq.heapify(nums)

    def add(self, val: int) -> int:
        print(self.heap)
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.max_size:
            heapq.heappop(self.heap)
        return self.heap[0]
        
        
