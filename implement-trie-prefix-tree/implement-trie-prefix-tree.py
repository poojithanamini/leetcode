class Trie:

    def __init__(self):
        self.d = {}
        self.prefix_d = {}
    def insert(self, word: str) -> None:
        self.d[word] = True
        for i in range(len(word)+1):
            self.prefix_d[word[:i]] = True

    def search(self, word: str) -> bool:
        return word in self.d

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix_d