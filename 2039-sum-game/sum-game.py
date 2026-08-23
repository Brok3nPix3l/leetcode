class Solution:
    class SumGameString:
        def __init__(self, s: str):
            n = len(s)
            
            self.firstHalfQuestionMarkCount = s.count('?', 0, n // 2)
            self.secondHalfQuestionMarkCount = s.count('?', n // 2, n)

            self.firstHalfDigitSum = sum(int(s[i]) if s[i] != '?' else 0 for i in range(n // 2))
            self.secondHalfDigitSum = sum(int(s[i]) if s[i] != '?' else 0 for i in range(n // 2, n))
    
    def sumGame(self, num: str) -> bool:
        s = self.SumGameString(num)
        # if the sum of the digits in one half of the string, s1, is less than the number of question marks in excess in the second half of the string, q2 - q1, times 9, then Alice will win
        if ((s.firstHalfQuestionMarkCount - s.secondHalfQuestionMarkCount) // 2) * 9 > s.secondHalfDigitSum - s.firstHalfDigitSum:
            return True
        if ((s.secondHalfQuestionMarkCount - s.firstHalfQuestionMarkCount) // 2) * 9 > s.firstHalfDigitSum - s.secondHalfDigitSum:
            return True
        # if there is an odd number of question marks, Bob will win
        return abs(s.firstHalfQuestionMarkCount - s.secondHalfQuestionMarkCount) % 2 == 1