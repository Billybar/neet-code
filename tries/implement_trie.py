class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {} # hashmap char-> TrieNode
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        trie_node = self.root

        for char in word:
            if char not in trie_node.children:
                return False
            trie_node = trie_node.children[char] # move to next child node

        if trie_node.end_of_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        trie_node = self.root

        for char in prefix:
            if char not in trie_node.children:
                return False
            trie_node = trie_node.children[char] # move to next child node

        return True
