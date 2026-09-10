class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        smallest_index, longest_duration = events[0]
        prev_time = longest_duration

        for cur_index, cur_time in events[1:]:
            cur_duration = cur_time - prev_time

            if cur_duration > longest_duration:
                longest_duration = cur_duration
                smallest_index = cur_index
            elif cur_duration == longest_duration:
                smallest_index = min(smallest_index, cur_index)
            
            prev_time = cur_time
        
        return smallest_index