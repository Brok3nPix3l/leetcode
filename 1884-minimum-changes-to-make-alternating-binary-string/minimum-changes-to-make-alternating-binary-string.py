class Solution:
    def minOperations(self, s: str) -> int:
        keep_first_digit_ops = 0
        cur = s[0]
        for d in s[1:]:
            cur = '0' if cur == '1' else '1'
            # print(f'd={d} cur={cur}')
            if d != cur:
                keep_first_digit_ops += 1
        # print(f'keep_first_digit_ops={keep_first_digit_ops}')
        change_first_digit_ops = 1
        cur = '0' if s[0] == '1' else '1'
        for d in s[1:]:
            cur = '0' if cur == '1' else '1'
            print(f'd={d} cur={cur}')
            if d != cur:
                change_first_digit_ops += 1
        # print(f'change_first_digit_ops={change_first_digit_ops}')
        return min(keep_first_digit_ops, change_first_digit_ops)