import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        heapq.heapify(arr)

        for point in points:
            heapq.heappush(arr, [-(point[0]**2 + point[1]**2), point])
            if len(arr) > k:
                heapq.heappop(arr)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res