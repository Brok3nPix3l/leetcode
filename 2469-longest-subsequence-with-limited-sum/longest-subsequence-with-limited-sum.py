class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre = [nums[0]]
        for num in nums[1:]:
            pre.append(pre[-1] + num)
        ans = [len(pre) for _ in queries]
        queryIdxDict = {}
        for i, q in enumerate(queries):
            queryIdxDict.setdefault(q, []).append(i)
        # print(f'pre={pre} ans={ans} queryIdxDict={queryIdxDict}')
        queries.sort()
        qIdx = 0
        preIdx = 0
        while qIdx < len(queries) and preIdx < len(pre):
            while pre[preIdx] > queries[qIdx]:
                # print(f'pre[{preIdx}]={pre[preIdx]} queries[{qIdx}]={queries[qIdx]}')
                for i in queryIdxDict[queries[qIdx]]:
                    ans[i] = preIdx
                    qIdx += 1
                if qIdx >= len(queries):
                    break
            preIdx += 1
        
        return ans