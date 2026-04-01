import heapq
class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.mini, -num)
        heapq.heappush(self.maxi, -heapq.heappop(self.mini))

        if abs(len(self.maxi) - len(self.mini)) > 1:
            heapq.heappush(self.mini, -heapq.heappop(self.maxi))
        

    def findMedian(self) -> float:
        if len(self.mini) == len(self.maxi):
            return (-self.mini[0] + self.maxi[0])/2
        return self.mini[0] if len(self.mini) > len(self.maxi) else self.maxi[0]
        