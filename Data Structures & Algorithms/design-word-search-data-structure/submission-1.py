class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:  # ✅ Check first
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(node, word, idx):
            # Base case: reached end of word
            if idx == len(word):
                return node.endOfWord
            
            char = word[idx]
            
            if char == '.':
                # Try ALL children
                for child in node.children.values():
                    if dfs(child, word, idx + 1):
                        return True
                return False
            else:
                # Try the specific character
                if char in node.children:
                    return dfs(node.children[char], word, idx + 1)
                return False
            
            
        return dfs(self.root, word, 0)
