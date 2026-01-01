class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ptr = len(digits) - 1
        digits[ptr] += 1
        while digits[ptr] == 10 and ptr > 0:
            digits[ptr] = 0
            digits[ptr-1] += 1
            ptr -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits