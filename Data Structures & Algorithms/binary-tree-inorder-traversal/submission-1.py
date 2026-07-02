# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorderdfs(root, result):
            if not root:
                return
            inorderdfs(root.left,result)
            result.append(root.val)
            inorderdfs(root.right,result)
        inorderdfs(root,res)

        return res
        