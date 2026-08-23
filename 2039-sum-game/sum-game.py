class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        q1 = num.count('?', 0, n // 2)
        q2 = num.count('?', n // 2, n)

        s1 = sum(int(num[i]) if num[i] != '?' else 0 for i in range(n // 2))
        s2 = sum(int(num[i]) if num[i] != '?' else 0 for i in range(n // 2, n))

        # if the sum of the digits in one half of the string, s1, is less than the number of question marks in excess in the second half of the string, q2 - q1, times 9, then Alice will win
        if ((q1 - q2) // 2) * 9 > s2 - s1:
            return True
        if ((q2 - q1) // 2) * 9 > s1 - s2:
            return True
        # if there is an odd number of question marks, Bob will win
        return abs(q1 - q2) % 2 == 1