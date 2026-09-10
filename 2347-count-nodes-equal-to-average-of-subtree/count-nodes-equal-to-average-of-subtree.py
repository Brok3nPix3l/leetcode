# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def traverse(node: TreeNode) -> Tuple[int, int]:
            nonlocal ans
            s, c = node.val, 1
            
            if node.left != None:
                ns, nc = traverse(node.left)
                s += ns
                c += nc
            if node.right != None:
                ns, nc = traverse(node.right)
                s += ns
                c += nc
            
            if node.val == s // c:
                ans += 1
            
            # print('node', node.val, 's', s, 'c', c)
            
            return s, c

        traverse(root)
        return ans