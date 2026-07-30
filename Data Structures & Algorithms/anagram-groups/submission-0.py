class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # will create a map : key hash value list
        table = {}
        a = ord('a')
        for st in strs:
            # create a string hash
            sig_table = [0] * 26
            for ch in st:
               sig_table[ ord(ch) - a ] +=1
            key = tuple(sig_table)
            # check if hash is present, else add
            if key in table:
                table[key].append( st )
            else:
                table[key] = [st]
        # now result
        return list( table.values())