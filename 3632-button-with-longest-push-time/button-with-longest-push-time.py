class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        smallest_index, longest_duration = events[0]
        prev_time = longest_duration

        for i in range(1, len(events)):
            cur_index, cur_time = events[i]
            prev_time = events[i - 1][1]
            cur_duration = cur_time - prev_time

            if cur_duration > longest_duration:
                longest_duration = cur_duration
                smallest_index = cur_index
            elif cur_duration == longest_duration and cur_index < smallest_index:
                smallest_index = cur_index
            
            prev_time = cur_time
        
        return smallest_index