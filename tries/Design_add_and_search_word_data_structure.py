class TrieNode:
    def __init__(self):
        self.children: dict[str,TrieNode] = {}
        self.end_of_word = False

    def __repr__(self):
        return f"Node(keys={list(self.children.keys())}, end={self.end_of_word})"

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        trie_node = self.root # strat iterate form root

        #if char exsit go to exsit char else: add new one
        for char in word:
            if char not in trie_node.children:
                trie_node.children[char] = TrieNode()
            trie_node = trie_node.children[char] # move to next node
        trie_node.end_of_word = True

    def search(self, word: str) -> bool:

        def dfs(node, sub_word):
            for i, char in enumerate(sub_word):
                if char == '.':
                    # If the character is '.', iterate through all possible children
                    for child in node.children.values():
                        # Recursively search the remaining substring starting from the next character
                        if dfs(child, sub_word[i + 1:]):
                            return True
                    return False  # No path matched the pattern

                # Standard character handling
                if char not in node.children:
                    return False

                # Move to the next node in the Trie
                node = node.children[char]

            # After processing the entire word, check if it marks the end of a valid word
            return node.end_of_word

        # Start the search from the root node
        return dfs(self.root, word)

words = ["WordDictionary","addWord","example","search","e.ap.e"]
tree = WordDictionary()

tree.addWord("day")
tree.addWord("bay")
tree.addWord("may")
tree.search("say") # return false
tree.search("day") # return true
tree.search(".ay") # return true
tree.search("b..") # return true