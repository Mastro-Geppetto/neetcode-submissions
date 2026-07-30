class Solution:

    def encode(self, strs: List[str]) -> str:
        # scheme strlen+string
        result = ''
        for s in strs:
            l = len(s)
            result += str(l)
            result += '+'
            result += s
        #print(result)
        return result

    def decode(self, s: str) -> List[str]:
        # scheme strlen+string
        result = []
        if not len(s):
            return result
        print(s)
        c_pos = 0
        while c_pos < len(s):
            p_pos = s.find('+', c_pos)
            #print("sub:", c_pos, p_pos, s[c_pos : p_pos])
            size = int(s[c_pos : p_pos])
            #print('start:',p_pos, size)
            c_pos = p_pos+1
            result.append( s[c_pos: c_pos+size])
            c_pos = c_pos+size
            #print('final:',c_pos)
        #print(result)
        return result
