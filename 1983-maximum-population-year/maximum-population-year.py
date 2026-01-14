import heapq

class Solution:
    START_YEAR = 1950
    END_YEAR = 2050

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = 0
        min_max_pop_year = self.START_YEAR
        
        population_during_year = [0 for y in range(self.END_YEAR - self.START_YEAR + 1)]
        for log in logs:
            population_during_year[log[0] - self.START_YEAR] += 1
            population_during_year[log[1] - self.START_YEAR] -= 1
        # print(population_during_year)

        cur_pop = 0
        for year_offset, population in enumerate(population_during_year):
            cur_pop += population
            if cur_pop > max_pop:
                max_pop = cur_pop
                min_max_pop_year = year_offset + self.START_YEAR
        
        return min_max_pop_year