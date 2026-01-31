class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        while l < r:
            m = (r + l) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1
        
        if letters[r] > target:
            return letters[r]
        else:
            return letters[0]