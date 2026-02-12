class Solution:
    def longestBalanced(self, s: str) -> int:
        for size in range(len(s), 1, -1):
            c = Counter(s[0:size])
            l = 0
            # print(f'size={size} substring={s[0:size]} c={c}')
            if len(set(c.values())) == 1:
                return size
            for r in range(size, len(s)):
                c[s[l]] -= 1
                l += 1
                c[s[r]] += 1
                # print(f'l={l} r={r} substring={s[l:r]} c={c}')
                if len(set(v for v in c.values() if v > 0)) == 1:
                    return size
        return 1