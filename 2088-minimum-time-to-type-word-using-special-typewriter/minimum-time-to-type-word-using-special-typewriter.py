class Solution:
    WHEEL_SPACES = (ord('z') - ord('a') + 1)

    def minTimeToType(self, word: str) -> int:
        cur = 'a'
        time = 0
        for c in word:
            clockwise_time = (ord(c) - ord(cur)) % self.WHEEL_SPACES
            counterclockwise_time = (ord(cur) - ord(c)) % self.WHEEL_SPACES
            # print(f'{cur}->{c} clockwise_time={clockwise_time} counterclockwise_time={counterclockwise_time}')
            if clockwise_time < counterclockwise_time:
                time_taken = clockwise_time
            else:
                time_taken = counterclockwise_time
            
            time += time_taken + 1
            cur = c
        
        return time