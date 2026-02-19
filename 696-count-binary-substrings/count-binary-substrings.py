class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = 0
        m = 0
        ans = 0
        for r in range(len(s)):
            # print(f'l={l} m={m} r={r}')
            if s[r] != s[m]:
                if l != m:
                    ans += min(r - m, m - l)
                l = m
                m = r
                # print(f'l={l} m={m} r={r} ans={ans}')
        ans += min(len(s) - m, m - l)
        return ans