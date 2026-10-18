class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        """
        sort the array based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

        map each num to a tuple of (sum of digits, num), then sort
        """
        def to_sorting_key(num: int) -> int:
            return (sum(int(c) for c in str(num)), num)

        # create new sorted list by mapping source indices to target indices
        target_indices = sorted(range(len(nums)), key=lambda i: to_sorting_key(nums[i]))
        # print(target_indices)
        

        """
        use union-find to map each num to its connected component

        use -1 to indicate that a num maps to itself; filter out later

        if a cycle is present, all elements will be set to the lowest index in the cycle (technically it's just the first index accessed, but since we're traversing in ascending order, it'll also be the lowest)
        """
        parent = [None] * len(nums)
        def add_to_parent(i: int) -> None:
            if parent[i] is not None:
                return
            
            parent[i] = -1
            target_idx = target_indices[i]
            add_to_parent(target_idx)
            
            if parent[target_idx] == -1:
                if target_idx != i:
                    parent[i] = target_idx
            else:
                parent[i] = parent[target_idx]

        for i in range(len(nums)):
            add_to_parent(i)
        
        # print(parent)


        """
        the minimum number of swaps to sort the array is n - number_of_cycles in the permutation.
        """
        diff = [i for i in parent if i != -1]
        nums_to_move = len(diff)
        cycle_count = len(set(diff))
        return nums_to_move - cycle_count