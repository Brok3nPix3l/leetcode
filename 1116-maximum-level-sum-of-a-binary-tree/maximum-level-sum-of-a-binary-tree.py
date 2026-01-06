# initalize dict of level -> sum
# traverse tree and add each node's value to its level's sum
# return the minimum level with the maximum sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def traverse_tree(node: Optional[TreeNode], level: int, level_sums: dict[int, int]) -> None:
            level_sums[level - 1] += node.val
            if node.left:
                traverse_tree(node.left, level + 1, level_sums)
            if node.right:
                traverse_tree(node.right, level + 1, level_sums)
        
        level_sums = defaultdict(int)
        traverse_tree(root, 1, level_sums)
        
        max_sum = root.val
        min_max_level = 1
        for level, sum in level_sums.items():
            if sum > max_sum:
                # print(f'new max sum {sum} on level {level}')
                max_sum = sum
                min_max_level = level + 1
        
        return min_max_level