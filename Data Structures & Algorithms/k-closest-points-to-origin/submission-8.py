import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # keep heap of size k -> return every set of points in the heap
        # max-heap of size k
        #if the distance is smaller than the top, then push into the heap, and then pop the top
        heap = []
        for point in points:
            # find distance sqrt((x1 - x2)^2 + (y1 - y2)^2)
            distance = point[0]**2 + point[1]**2

            heapq.heappush(heap, (-distance, point))         

            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
