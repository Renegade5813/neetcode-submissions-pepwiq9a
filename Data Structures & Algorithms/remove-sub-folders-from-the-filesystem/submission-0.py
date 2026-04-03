import heapq
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isFolder = False
    
    def add(self, element):
        for i in element.split('/')[1:]:
            if i not in self.children:
                self.children[i] = Trie()
            self = self.children[i]
        self.isFolder = True

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #for each element in input list, use .split('/') for the string
        #check if Trie has each element of the sublist
        root = Trie()
        for i in range(len(folder)):
            root.add(folder[i])
            
        def hasParent(path):
            node = root
            parts = [part for part in path.split('/') if part != ""]
            
            for i in range(len(parts)):
                node = node.children[parts[i]]
                
                if node.isFolder and i != len(parts) - 1:
                    return True
            return False
        
        ans = []
        for f in folder:
            if not hasParent(f):
                ans.append(f)
        
        return ans
        