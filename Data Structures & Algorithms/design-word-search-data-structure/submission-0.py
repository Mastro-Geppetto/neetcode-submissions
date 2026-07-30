class tries_node:
    def __init__(self):
        '''
        tries : char [children:dict & end_of_word:flag]
        '''
        self.children = dict()
        self.end_of_word = False
class WordDictionary:
    def __init__(self):
        self.root = tries_node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                # absent, add
                curr.children[c] = tries_node()
            # go down
            curr = curr.children[c]
        # mark last one as end
        curr.end_of_word = True
    def __internal_search__(self, root, word) -> bool:
        if not len(word):
            print("\tSear:",root,"\n",root.end_of_word)
            return root.end_of_word
        if word[0] in root.children:
            # go down
            return self.__internal_search__(
                        root.children[word[0]],
                        word[1:])
        if word[0] == '.':
            return any(
                [\
                self.__internal_search__(root.children[k], word[1:]) \
                for k in root.children.keys()]
            )
        # else
        return False
    def search(self, word: str) -> bool:
        '''
        in case of "."
        we will have to check ALL char position
        '''
        curr = self.root
        return self.__internal_search__(self.root, word)
                    