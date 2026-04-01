import heapq
class MedianFinder:

    def __init__(self):
        self.mini = []
        self.maxi = []

    def addNum(self, num: int) -> None:

        if not self.maxi and not self.mini: # first number
            heapq.heappush(self.maxi, num)
            return
        
        heapq.heappush(self.mini, -num)
        print("first",self.mini, self.maxi)
        if -self.mini[0] > self.maxi[0]:
            heapq.heappush(self.maxi, -heapq.heappop(self.mini))
        print("second",self.mini, self.maxi)
        if abs(len(self.mini) - len(self.maxi)) > 1:
            if len(self.mini) > len(self.maxi):
                heapq.heappush(self.maxi, -heapq.heappop(self.mini))
            else:
                heapq.heappush(self.mini, -heapq.heappop(self.maxi))
            
        print(self.mini, self.maxi)



    def findMedian(self) -> float:
        if len(self.mini) == len(self.maxi):
            tmp1 = -self.mini[0]
            tmp2 = self.maxi[0]
            return (tmp1+tmp2)/2
        if len(self.mini) > len(self.maxi):
            return -self.mini[0]
        else:
            return self.maxi[0]
        