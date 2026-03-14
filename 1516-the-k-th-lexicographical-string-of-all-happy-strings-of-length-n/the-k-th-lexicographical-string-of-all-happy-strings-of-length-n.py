class Solution:
    def __init__(self):
        self.happyStrings = []
        self.kthHappyString = None

    def getHappyString(self, n: int, k: int) -> str:
        return self.appendHappyStrings(n, k, '') or ''
    
    def appendHappyStrings(self, n: int, k: int, s: str) -> Union[str, None]:
        if len(s) == n:
            self.happyStrings.append(s)
            if len(self.happyStrings) == k:
                self.kthHappyString = s
            return s
        
        if len(s) == 0 or s[-1] != 'a':
            self.appendHappyStrings(n, k, s + 'a')
        if self.kthHappyString:
            return self.kthHappyString
        if len(s) == 0 or s[-1] != 'b':
            self.appendHappyStrings(n, k, s + 'b')
        if self.kthHappyString:
            return self.kthHappyString
        if len(s) == 0 or s[-1] != 'c':
            self.appendHappyStrings(n, k, s + 'c')
        if self.kthHappyString:
            return self.kthHappyString