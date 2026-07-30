class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for i in nums:
            table[i] = table.get( i, 0) + 1
        # transform frequent elements
        dump = [ (v,k) for k,v in table.items() ]
        dump.sort(reverse=True)
        print(dump)
        # find k most frequent elements
        result = []
        for i in range(k):
            result.append( dump[i][-1] )
        return list(result)
