class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        for d in str(n):
            if d != '0':
                x += d
        if x == '':
            x = '0'
        # print(x)
        s = sum(int(d) for d in x)
        # print(s)
        return int(x) * s