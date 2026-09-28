class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxDepth = 0

        for c in s:
            match c:
                case '(':
                    depth += 1
                    maxDepth = max(maxDepth, depth)
                case ')':
                    depth -= 1
        
        return maxDepth