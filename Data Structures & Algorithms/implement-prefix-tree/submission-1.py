class TrieNode: 
    def __init__(self, value = "", flag = False):
        self.pointers = {}
        self.flag = flag #marks end of each word

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for i, char in enumerate(word):
            if char not in cur.pointers:
                cur.pointers[char] = TrieNode(value = char)

            cur = cur.pointers[char]

            if i == len(word) - 1:
                cur.flag = True


    def search(self, word: str) -> bool:
        cur = self.root

        for char in word:
            if char not in cur.pointers:
                return False
        
            cur = cur.pointers[char]

        return cur.flag
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.pointers:
                return False
        
            cur = cur.pointers[char]

        return True