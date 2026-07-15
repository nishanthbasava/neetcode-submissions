class TrieNode:
    def __init__(self, flag=False):
        self.pointers = {}
        self.flag = flag

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.pointers:
                cur.pointers[char] = TrieNode()
            cur = cur.pointers[char]

        cur.flag = True
    

    #what about searching for words with dots in them 
    def search(self, word: str) -> bool:
        def dfs(node, remaining):
            if len(remaining) == 0:
                return node.flag

            char = remaining[0]

            if char == ".":
                for child in node.pointers.values():
                    if dfs(child, remaining[1:]):
                        return True
                return False

            if char not in node.pointers:
                return False

            return dfs(node.pointers[char], remaining[1:])

        return dfs(self.root, word)