class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = "".join(d for d in str(n) if d != '0')
        if x == '':
            x = '0'
            # return 0
        # print(x)
        s = sum(int(d) for d in x)
        # print(s)
        return int(x) * s