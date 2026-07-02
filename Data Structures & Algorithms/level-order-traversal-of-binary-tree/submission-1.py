# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result=[]
        if not root:
            return []
        level=0
        queue.append(root)
        while len(queue)>0:
            level+=1
            cur_res=[]
            for i in range(len(queue)):
                current= queue.popleft()
                cur_res.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(cur_res)
        return result
            
            
        