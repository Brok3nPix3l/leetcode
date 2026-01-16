class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_segment = [0, 0]
        cur_num = s[0]
        cur_len = 0
        l = 0
        for r in range(len(s)):
            if s[r] == cur_num:
                cur_len += 1
                continue
            else:
                longest_segment[int(cur_num)] = max(longest_segment[int(cur_num)], cur_len)
                cur_num = s[r]
                cur_len = 1
        
        longest_segment[int(cur_num)] = max(longest_segment[int(cur_num)], cur_len)
        
        return longest_segment[1] > longest_segment[0]