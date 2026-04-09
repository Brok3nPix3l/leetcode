class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        l, r = startIndex, startIndex
        lte, gte = False, False
        for steps in range(ceil(len(words) / 2) + 1):
            # print(f'steps={steps} words[{l}]={words[l]} words[{r}]={words[r]}')
            if words[l] == target or words[r] == target:
                return steps
            l = (l - 1 + n) % n
            r = (r + 1) % n
        return -1