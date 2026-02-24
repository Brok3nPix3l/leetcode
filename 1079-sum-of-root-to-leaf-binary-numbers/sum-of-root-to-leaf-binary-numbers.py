# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.sum
        
    def helper(self, node: Optional[TreeNode], cur: int) -> None:
        if node == None:
            return
        cur <<= 1
        cur += node.val
        if node.left == None and node.right == None:
            # print(cur)
            self.sum += cur
            return
        # print(f'node.val == {node.val}')
        self.helper(node.left, cur)
        self.helper(node.right, cur)
        