class MedianFinder:

    def __init__(self):
        # left side
        self.max_heap = []
        heapq.heapify_max(self.max_heap)
        # right side
        self.min_heap = []
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        if len(self.max_heap) and num > self.max_heap[0]:
            # push on right
            heapq.heappush(self.min_heap, num)
        else:
            # push on left
            heapq.heappush_max(self.max_heap, num)
        # check for size inequality
        if len(self.max_heap) >= len(self.min_heap)+2:
            print("rebalance max_heap")
            item = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, item)
        elif len(self.min_heap) >= len(self.max_heap)+2:
            print("rebalance min_heap")
            item = heapq.heappop(self.min_heap)
            heapq.heappush_max(self.max_heap, item)
        print("insert", self.max_heap, self.min_heap)

    def findMedian(self) -> float:
        print("find", self.max_heap, self.min_heap)
        if len(self.min_heap) == len(self.max_heap):
            return (self.max_heap[0]+self.min_heap[0])/2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return self.max_heap[0]
        