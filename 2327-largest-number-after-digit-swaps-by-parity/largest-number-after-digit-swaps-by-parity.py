class Solution:
    def largestInteger(self, num: int) -> int:
        s = str(num)
        idxParity = []
        evenDigits = []
        oddDigits = []
        for i, ds in enumerate(s):
            d = int(ds)
            if d % 2 == 0:
                evenDigits.append(d)
            else:
                oddDigits.append(d)
        evenDigits.sort(reverse=True)
        oddDigits.sort(reverse=True)
        # print(f'evenDigits={evenDigits} oddDigits={oddDigits}')
        ans = 0
        for i, d in enumerate(s):
            ans *= 10
            if int(d) % 2 == 0:
                ans += evenDigits[0]
                evenDigits.pop(0)
            else:
                ans += oddDigits[0]
                oddDigits.pop(0)
        return ans