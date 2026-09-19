class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        pre = prefixArr(nums)
        # print(pre)
        ans = 0
        
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            # print(start, i)
            # print(sum(nums[start:i + 1]), pre[i] - pre[start])
            ans += pre[i + 1] - pre[start]
        
        return ans

def prefixArr(nums: List[int]) -> List[int]:
    cur = 0
    arr = [0] * (len(nums) + 1)

    for i, num in enumerate(nums):
        cur += num
        arr[i + 1] = cur
    
    return arr