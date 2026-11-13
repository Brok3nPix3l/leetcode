class Solution:
    def scoreBalance(self, s: str) -> bool:
        total_score = sum(ord(c) - ord('a') + 1 for c in s)
        if total_score % 2 == 1:
            return False

        target_prefix_score = total_score // 2
        
        prefix_score = 0
        for i, c in enumerate(s):
            prefix_score += ord(c) - ord('a') + 1
            # print(f'{i} {c} {prefix_score}')
            if prefix_score == target_prefix_score:
                return True
            elif prefix_score > target_prefix_score:
                return False
        
        return False