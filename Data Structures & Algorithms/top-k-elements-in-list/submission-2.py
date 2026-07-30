class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in nums:
            table[i] = table.get( i, 0) + 1
        # min-heap
        heap = []
        # for each number
        for num in table.keys():
            heapq.heappush(
                heap,
                (table[num], num) # priority - value
            )
            # retain the top k elements
            if len(heap) > k:
                heapq.heappop(heap)
        # create result
        result = []
        for i in range(k):
            # append only the number
            result.append( heapq.heappop(heap)[-1] )
        return result
