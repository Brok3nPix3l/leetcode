class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest_duration, smallest_index = None, None

        for i, (index, time) in enumerate(events):
            if i == 0:
                cur_duration = time
            else:
                cur_duration = time - events[i - 1][1]

            if longest_duration is None or cur_duration > longest_duration:
                longest_duration = cur_duration
                smallest_index = index
            elif longest_duration == cur_duration and index < smallest_index:
                smallest_index = index
        
        return smallest_index