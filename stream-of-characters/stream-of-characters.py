class TrieTree:
    def __init__(self):
        self.root = {}
    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        while i < len(word):
            if word[i] in node:
                node = node[word[i]]
                i += 1
                continue
            break        
        while i < len(word):
            node[word[i]] = {}
            node = node[word[i]]
            i+=1
		# mark it as the last character of a word
        node["$"]={}
        return
     # Check whether the stream suffix existed on tree or not
	 # Can reverse suffix, so we check it like prefix
    def isPrefix(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            if "$" in node[c]:
                return True
            node = node[c]
        return False
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = ""
        self.trie = TrieTree()
        for w in words:
			# because we need to check suffix, so reversing the word
            self.trie.insert(w[::-1])
        print(self.trie.root)

    def query(self, letter: str) -> bool:
        self.stream += letter
        return self.trie.isPrefix(self.stream[::-1])