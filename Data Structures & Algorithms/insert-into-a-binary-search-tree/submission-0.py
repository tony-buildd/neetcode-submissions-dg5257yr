# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root

        # base case: no more node
        if not root:
            return TreeNode(val)

        # val is larger so go to the right
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # val is smaller so go to the left
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return head
        
