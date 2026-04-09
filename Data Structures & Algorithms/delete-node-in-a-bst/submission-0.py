class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMinNode(root):
            while root and root.left:
                root = root.left
            return root

        top = root

        # base case
        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # value found to delete
        else:
            # case 1: root has 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # case 2: root has 2 child
            else:
                # search for the smallest root of the right subtree
                minNode = findMinNode(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
            
        return top