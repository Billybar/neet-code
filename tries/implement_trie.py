class TrieNode:
    def __init__(self):
        self.children = {} # hashmap char-> TrieNode
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root =TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur =cur.children[char]

    def search(self, word: str) -> bool:

    def startsWith(self, prefix: str) -> bool:

