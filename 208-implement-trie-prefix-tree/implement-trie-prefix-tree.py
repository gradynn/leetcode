class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.keys():
                cur[c] = {}
            cur = cur[c]
        cur["$"] = {}

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.keys():
                return False
            cur = cur[c]
        if "$" in cur.keys():
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.keys():
                return False
            cur = cur[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)