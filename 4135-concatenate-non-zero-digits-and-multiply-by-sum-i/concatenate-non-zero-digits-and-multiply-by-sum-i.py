class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = "".join(d for d in str(n) if d != '0')
        if x == '':
            """
            - x == '0'
            - s = 0
            - int(x) * s == 0 * 0 == 0
            """
            return 0
        s = sum(int(d) for d in x)
        return int(x) * s