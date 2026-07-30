class PrefixTree:

    def __init__(self):
        '''
        Tries : dict key=26 char -vs- [True/False, embedded dict]
            the True/False : End of word/Not end of word
        '''
        self.tries = dict()
    
    def insert(self, word: str) -> None:
        head = self.tries
        for c in word[:-1]:
            # skipping last char, as we use it to mark end of word
            if c not in head:
                head[c] = [False,dict()]
            head = head[c][-1]
        # last char
        c = word[-1]
        if c not in head:
            head[c]=[False,dict()]
        head[c][0]=True

    def search(self, word: str) -> bool:
        head = self.tries
        for c in word[:-1]:
            if c not in head:
                return False
            head = head[c][-1]
        # last char
        c = word[-1]
        if c not in head or not head[c][0]:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        # similar to search, skip end check
        head = self.tries
        for c in prefix[:-1]:
            if c not in head:
                return False
            head = head[c][-1]
        # last char
        c = prefix[-1]
        if c not in head:
            return False
        return True