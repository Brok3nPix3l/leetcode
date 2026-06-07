# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        isChild = set()
        seen = set()
        nodes = {}
        for parent, child, isLeft in descriptions:
            seen.add(parent)
            seen.add(child)
            isChild.add(child)
            if parent not in nodes:
                parentNode = TreeNode(val=parent)
                nodes[parent] = parentNode
            else:
                parentNode = nodes[parent]
            if child not in nodes:
                childNode = TreeNode(val=child)
                nodes[child] = childNode
            else:
                childNode = nodes[child]
            if isLeft:
                parentNode.left = childNode
            else:
                parentNode.right = childNode
        return nodes[next(iter(seen - isChild))]