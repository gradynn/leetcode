class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode.children.keys():
                newNode = TrieNode()
                curNode.children[c] = newNode
                curNode = newNode
            else:
                curNode = curNode.children[c]
        curNode.isEnd = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word:
            if c not in curNode.children.keys():
                return False
            curNode = curNode.children[c]
        if curNode.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for c in prefix:
            if c not in curNode.children.keys():
                return False
            curNode = curNode.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)