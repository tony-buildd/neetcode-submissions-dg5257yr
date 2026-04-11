# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        - counting level of left and right node of a node then compare
        - count and compare the same time by using postorder

        1:
            - left node: 2
                - left node: null
            left count:1
            - right node:3
                left node: 4
                    left node: null
                left count: 1
                right node: null
            - right count: max(left, right) = 1
        - abs(left - right) > 1: false else true
            
        '''
        def postOrderTraversal(root, count):
            '''
            POT(1,0)
            - left = POT(2, 0) + 1 = 1 + 1 = 2
                - left = POT(null, 0) + 1 = 0 + 1 = 1
                - right = POT(null, 0) + 1 = 0 + 1 = 1
                - abs(left - right) == False
                - count = 1

            - right = POT(3, 0) + 1 = 2
                - left = POT(4,1) + 1 = 2 + 1 = 3
                    - left = POT(5, 0) + 1  = 1 + 1 = 2
                        - left = POT(null, 0) + 1 = 0 + 1 = 1
                        - right = POT(null, 0) + 1 = 0 + 1 = 1
                        - abs = False
                        - count = 1
                    - right = POT(null, 0) + 1 = 1
                    - abs(1 - 2) !> 1 -> false
                    - count = max(1,2) = 2
                - right = POT(null,0) + 1 = 0 + 1 = 1
                - abs(3 - 1) = 2 > 1: True -> return -1
            - abs(left - right) = ab(1-2) = 1 -> False
            - count = 2
            '''
            if not root:
                return 0
            left_height = postOrderTraversal(root.left, count)
            right_height = postOrderTraversal(root.right, count)
            if left_height == -1 or right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1
        
        if postOrderTraversal(root, 0) == -1:
            return False
        return True

            
