class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        delta = 1
        ans = 1
        for _ in range(time):
            ans += delta
            if ans == n or ans == 1:
                delta *= -1
            # print(f'ans={ans}')
            # print(f'delta={delta}')
        return ans