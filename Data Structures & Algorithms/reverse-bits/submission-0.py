class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        setter = (1<<31)
        mask = 1
        for i in range(32):
            #print(i,end=",")
            if n&mask:
                answer |= setter
                #print(1," a:", answer)
            #else:
            #    print(0)
            mask = mask << 1
            setter = setter >> 1
        return answer