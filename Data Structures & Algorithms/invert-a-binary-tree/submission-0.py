# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        swap from bottom up would be easier to maintain the structure, as once we
        swap the current one we don't have to worry about the structure below us
        - this approach would do post-order

        '''
        if not root:
            return None
        
        # traverse to the bottom 
        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root


        

    