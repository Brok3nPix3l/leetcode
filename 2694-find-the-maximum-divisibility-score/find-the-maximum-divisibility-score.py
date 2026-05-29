class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = 0
        max_score_divisor = divisors[0]
        for divisor in divisors:
            cur_score = 0
            for num in nums:
                if num % divisor == 0:
                    cur_score += 1
            if cur_score > max_score or cur_score == max_score and divisor < max_score_divisor:
                max_score = cur_score
                max_score_divisor = divisor
        return max_score_divisor