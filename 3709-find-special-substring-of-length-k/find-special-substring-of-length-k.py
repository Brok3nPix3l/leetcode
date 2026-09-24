class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)
        
        for i in range(n - k + 1):
            # print(f'i={i}')
            if i > 0:
                if s[i - 1] == s[i]:
                    # print(f's[{i - 1}] == s[{i}]')
                    continue
            
            if i + k < n:
                if s[i + k] == s[i + k - 1]:
                    # print(f's[{i + k}] == s[{i + k - 1}]')
                    continue
            
            def isAllSameChar(s: str) -> bool:
                # print(f'isAllSameChar s={s}')
                for i in range(len(s) - 1):
                    if s[i] != s[i + 1]:
                        # print(f's[{i}] != s[{i + 1}]')
                        return False
                
                return True

            if isAllSameChar(s[i:i + k]):
                return True
        
        return False