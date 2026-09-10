# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.ans

    def traverse(self, node: TreeNode) -> Tuple[int, int]:
        s, c = node.val, 1
        
        if node.left != None:
            ns, nc = self.traverse(node.left)
            s += ns
            c += nc
        if node.right != None:
            ns, nc = self.traverse(node.right)
            s += ns
            c += nc
        
        if node.val == s // c:
            self.ans += 1
        
        # print('node', node.val, 's', s, 'c', c)
        
        return s, c