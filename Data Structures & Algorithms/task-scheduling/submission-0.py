import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # freq count
        freq = [0] * 26
        heap = []
        queue = deque()
        time = 0

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        #populate heap
        for f in freq:
            if not f:
                continue
            heapq.heappush(heap, -f)
        #logic for queue and heap

        while heap or queue:
            time += 1
            if heap:
                task = heapq.heappop(heap) + 1
                if task:
                    queue.append([task, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time






