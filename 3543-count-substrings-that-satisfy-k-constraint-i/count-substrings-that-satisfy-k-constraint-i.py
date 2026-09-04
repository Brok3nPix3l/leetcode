class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        substringCount = 0
        
        bitsInWindow = [0] * 2
        l = 0
        for r, c in enumerate(s):
            bitsInWindow[int(s[r])] += 1
            while all(count > k for count in bitsInWindow):
                bitsInWindow[int(s[l])] -= 1
                l += 1

            substringCount += r - l + 1            
            # print('l', l, 'r', r)
            # print('bitsInWindow', bitsInWindow)
            # print('substringCount', substringCount)
        
        return substringCount