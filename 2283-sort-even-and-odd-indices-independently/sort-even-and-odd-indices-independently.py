class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [n for n in nums[::2]]
        odd = [n for n in nums[1::2]]
        # print(f'even={even}')
        # print(f'odd={odd}')
        even.sort()
        odd.sort(reverse=True)
        # print(f'sorted even={even}')
        # print(f'sorted odd={odd}')
        # print([even[-1]] if (len(even) > len(odd)) else [])
        return [n for pair in zip(even, odd) for n in pair] + ([even[-1]] if (len(even) > len(odd)) else [])