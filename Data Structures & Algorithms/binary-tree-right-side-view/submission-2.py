# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result=[]

        if not root:
            return []
        queue.append(root)
        level =0
        while len(queue)>0:
            result.append(queue[-1].val)
            level+=1
            for i in range(len(queue)):
                current= queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return result
