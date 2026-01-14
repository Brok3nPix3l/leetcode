class Solution:
    START_YEAR = 1950
    END_YEAR = 2050

    def maximumPopulation(self, logs: List[List[int]]) -> int:
        max_pop = 0
        min_max_pop_year = self.END_YEAR
        for y in range(self.START_YEAR, self.END_YEAR):
            cur_pop = self.population(y, logs)
            if cur_pop > max_pop:
                max_pop = cur_pop
                min_max_pop_year = y
        
        return min_max_pop_year

    def population(self, year: int, logs: List[List[int]]) -> int:
        pop = 0
        for log in logs:
            if log[0] <= year and log[1] > year:
                pop += 1

        return pop