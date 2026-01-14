import heapq

class Solution:
    START_YEAR = 1950
    END_YEAR = 2050

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = 0
        min_max_pop_year = self.END_YEAR
        alive_people = [] # contains death years. population is lenth of this heap during given year
        future_people = [] # contains people yet to be born. format is (birth year, death year)
        for log in logs:
            if log[0] <= self.START_YEAR:
                heapq.heappush(alive_people, log[1])
            else:
                heapq.heappush(future_people, (log[0], log[1]))
        
        # print(f'alive_people={alive_people} future_people={future_people}')
        cur_pop = len(alive_people)
        if cur_pop > max_pop:
            max_pop = cur_pop
            min_max_pop_year = self.START_YEAR

        for y in range(self.START_YEAR + 1, self.END_YEAR):
            while alive_people and alive_people[0] <= y:
                heapq.heappop(alive_people)
            
            while future_people and future_people[0][0] <= y:
                heapq.heappush(alive_people, heapq.heappop(future_people)[1])

            cur_pop = len(alive_people)
            if cur_pop > max_pop:
                max_pop = cur_pop
                min_max_pop_year = y
        
        return min_max_pop_year