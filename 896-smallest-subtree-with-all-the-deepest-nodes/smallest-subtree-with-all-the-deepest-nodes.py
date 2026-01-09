# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first pass: determine deepest node level and all deepest node level values
# second pass: iterate over each subtree to determine the one that contains all of the deepest node levels with the lowest node level itself
class Solution:
    deepest_node_level: int
    deepest_node_level_values: List[int]
    deepest_subtree_with_all_deepest_nodes: Optional[Tuple[TreeNode, int]]

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.deepest_node_level = 0
        self.deepest_node_level_values = []
        self.deepest_subtree_with_all_deepest_nodes = None
        
        self.determine_deepest_node_level_and_values_of_all_deepest_nodes(root, 0)
        self.determine_deepest_subtree_with_all_deepest_nodes(root, 0)
        
        if self.deepest_subtree_with_all_deepest_nodes:
            return self.deepest_subtree_with_all_deepest_nodes[0]
        return None
    
    def determine_deepest_node_level_and_values_of_all_deepest_nodes(self, node: Optional[TreeNode], depth: int) -> None:
        if depth > self.deepest_node_level:
            self.deepest_node_level = depth
            self.deepest_node_level_values = []
        if depth == self.deepest_node_level:
            self.deepest_node_level_values.append(node.val)
        
        if node.left:
            self.determine_deepest_node_level_and_values_of_all_deepest_nodes(node.left, depth + 1)
        
        if node.right:
            self.determine_deepest_node_level_and_values_of_all_deepest_nodes(node.right, depth + 1)
    
    def determine_deepest_subtree_with_all_deepest_nodes(self, node: Optional[TreeNode], depth: int) -> None:
        if node is None:
            return
        
        self.determine_if_subtree_has_all_deepest_nodes_and_is_deepest(node, depth)

        if node.left:
            self.determine_deepest_subtree_with_all_deepest_nodes(node.left, depth + 1)
        
        if node.right:
            self.determine_deepest_subtree_with_all_deepest_nodes(node.right, depth + 1)
        
    def determine_if_subtree_has_all_deepest_nodes_and_is_deepest(self, node: Optional[TreeNode], depth: int) -> None:
        if self.deepest_subtree_with_all_deepest_nodes and self.deepest_subtree_with_all_deepest_nodes[1] >= depth:
            return
        
        descendent_node_values = self.compile_all_descendent_node_values(node)
        has_all_nodes = True
        for deepest_node in self.deepest_node_level_values:
            if deepest_node not in descendent_node_values:
                has_all_nodes = False
                break
        
        if has_all_nodes:
            self.deepest_subtree_with_all_deepest_nodes = (node, depth)
    
    def compile_all_descendent_node_values(self, node: Optional[TreeNode]) -> Optional[Set[int]]:
        if node == None:
            return None
        
        nodes = set()
        
        nodes.add(node.val)

        if node.left:
            nodes.update(self.compile_all_descendent_node_values(node.left))
        
        if node.right:
            nodes.update(self.compile_all_descendent_node_values(node.right))
        
        return nodes