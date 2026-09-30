class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n = len(seq)
        ans = [0] * n

        cur = 0
        for i in range(1, n):
            if seq[i - 1] == seq[i]:
                cur = (cur + 1) % 2
            
            if cur == 1:
                ans[i] = 1
        
        return ans