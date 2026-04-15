class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        """
        use two pointers moving in opposite directions to find the target
        each pointer only needs to cover half of the array, since there's no overlap after the initial state
        if we don't manage to find the target during this, then it's not present at all
        """
        n = len(words)
        l, r = startIndex, startIndex
        for steps in range(floor(len(words) / 2) + 1):
            # print(f'steps={steps} words[{l}]={words[l]} words[{r}]={words[r]}')
            if words[l] == target or words[r] == target:
                return steps
            l = (l - 1 + n) % n
            r = (r + 1) % n
        return -1