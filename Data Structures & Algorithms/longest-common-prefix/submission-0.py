class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, element):
        curr = self.root
        for i in element:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.endOfWord = True
    
    def longestPrefix(self):
        prefix = []
        curr = self.root

        while len(curr.children) == 1 and not curr.endOfWord:
            char = next(iter(curr.children.keys()))
            prefix.append(char)
            curr = curr.children[char]
        return "".join(prefix)
            
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if any(s == "" for s in strs):
            return ""
        
        trie = Trie()
        for i in strs:
            trie.insert(i)

        return trie.longestPrefix()
        