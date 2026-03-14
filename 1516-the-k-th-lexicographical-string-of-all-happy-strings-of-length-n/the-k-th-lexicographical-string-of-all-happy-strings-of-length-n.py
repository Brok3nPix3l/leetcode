class Solution:
    def __init__(self):
        self.happyStrings = []

    def getHappyString(self, n: int, k: int) -> str:
        self.appendHappyStrings(n, '')
        # print(self.happyStrings)
        if len(self.happyStrings) >= k:
            return self.happyStrings[k-1]
        return ''
    
    def appendHappyStrings(self, n: int, s: str) -> None:
        if len(s) == n:
            # print(f's={s}')
            self.happyStrings.append(s)
            return
        
        if len(s) == 0 or s[-1] != 'a':
            self.appendHappyStrings(n, s + 'a')
        if len(s) == 0 or s[-1] != 'b':
            self.appendHappyStrings(n, s + 'b')
        if len(s) == 0 or s[-1] != 'c':
            self.appendHappyStrings(n, s + 'c')