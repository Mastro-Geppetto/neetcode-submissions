class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        a = ord('a')
        for i in range(len(s)):
            counter[ ord(s[i]) - a] += 1
            counter[ ord(t[i]) - a] -= 1
        #print(any(counter ), ":", counter)
        return not any(counter )