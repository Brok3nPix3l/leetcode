class Solution:
    def __init__(self):
        self.good_digits_set = {'2', '5', '6', '9'}
        self.bad_digits_set = {'3', '4', '7'}

    def rotatedDigits(self, n: int) -> int:
        # alternate phrasing of question: how many numbers in the range [1, n] contain a 2, 5, 6, and/or 9?
        return sum(1 if self.isGood(d) else 0 for d in range(1, n + 1))
    
    def isGood(self, x: int) -> bool:
        # x contains 1+ good digit and no bad digits
        s = set(str(x))
        # print(x, s.intersection(self.good_digits_set), s.intersection(self.bad_digits_set))
        return not s.isdisjoint(self.good_digits_set) and s.isdisjoint(self.bad_digits_set)