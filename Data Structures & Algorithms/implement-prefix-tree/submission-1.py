class tries_node:
    def __init__(self):
        '''
        nested list of 26 position (per char).
        Either None (absent) or pointer to next tries_node
        '''
        self.children = [None]*26
        self.end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = tries_node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = tries_node()
            curr = curr.children[idx]
        # mark last one
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        # check last one
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        # DON'T check last one
        return True
        