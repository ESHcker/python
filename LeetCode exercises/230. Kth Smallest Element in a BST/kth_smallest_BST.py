# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_tree = []
        def move_tree(root: Optional[TreeNode]):
            if root is None:
                return

            move_tree(root.left)
            ordered_tree.append(root.val)
            move_tree(root.right)
        move_tree(root)
        return ordered_tree[k - 1]
