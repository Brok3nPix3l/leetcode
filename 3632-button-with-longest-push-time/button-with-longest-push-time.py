class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        longest_duration, smallest_index = None, None

        def duration(i):
            nonlocal events
            cur_event_time = events[i][1]
            prev_event_time = events[i - 1][1]

            if i == 0:
                return cur_event_time
            
            return cur_event_time - prev_event_time
        
        for i, (index, time) in enumerate(events):
            cur_duration = duration(i)

            if longest_duration is None or cur_duration > longest_duration:
                longest_duration = cur_duration
                smallest_index = index
            elif longest_duration == cur_duration and index < smallest_index:
                smallest_index = index
        
        return smallest_index