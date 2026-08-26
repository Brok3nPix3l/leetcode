class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if k == 1:
            return "1" if s.count('1') > 0 else ""
        
        l = s.find('1')
        if l == -1:
            return ""
        ones = 0
        ans = None
        for r in range(l, len(s)):
            if s[r] == '1':
                ones += 1
            if ones == k:
                cur = s[l:r + 1]
                # print('cur', cur)
                if ans == None:
                    ans = cur
                else:
                    if len(cur) == len(ans):
                        ans = min(ans, cur)
                    elif len(cur) < len(ans):
                        ans = cur
                # print('ans', ans)
                l += 1
                while s[l] != '1':
                    l += 1
                ones -= 1
            # print('l', l, 'r', r, 'ones', ones)
        return ans or ""