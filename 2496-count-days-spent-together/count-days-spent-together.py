class Solution:
    def __init__(self):
        self.DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arrive, leave = self.determine_order((arriveAlice, leaveAlice), (arriveBob, leaveBob))
        # print(f'arrive={arrive} leave={leave}')
        return self.days_between(arrive[1][0], leave[0][1])


    def determine_order(self, a: Tuple[str, str], b: Tuple[str, str]) -> Tuple[Tuple[Tuple[str, str], Tuple[str, str]], Tuple[Tuple[str, str], Tuple[str, str]]]:
        a_arrive_month, a_arrive_day = (int(x) for x in a[0].split('-'))
        b_arrive_month, b_arrive_day = (int(x) for x in b[0].split('-'))
        a_leave_month, a_leave_day = (int(x) for x in a[1].split('-'))
        b_leave_month, b_leave_day = (int(x) for x in b[1].split('-'))
        # print(f'a: {a_arrive_month}/{a_arrive_day} -> {a_leave_month}/{a_leave_day}')
        # print(f'b: {b_arrive_month}/{b_arrive_day} -> {b_leave_month}/{b_leave_day}')
        
        if a_arrive_month < b_arrive_month:
            arrive = (a, b)
        elif b_arrive_month < a_arrive_month:
            arrive = (b, a)
        elif a_arrive_day < b_arrive_day:
            arrive = (a, b)
        elif b_arrive_day < a_arrive_day:
            arrive = (b, a)
        else:
            arrive = (a, b)
        
        if a_leave_month < b_leave_month:
            leave = (a, b)
        elif b_leave_month < a_leave_month:
            leave = (b, a)
        elif a_leave_day < b_leave_day:
            leave = (a, b)
        elif b_leave_day < a_leave_day:
            leave = (b, a)
        else:
            leave = (a, b)

        return (arrive, leave)

    def days_between(self, a: str, b: str) -> int:
        # print(f'days_between {a} and {b}')
        a_month, a_day = (int(x) for x in a.split('-'))
        b_month, b_day = (int(x) for x in b.split('-'))

        if a_month > b_month:
            return 0
        
        if a_month == b_month:
            if a_day > b_day:
                return 0
            if a_day == b_day:
                return 1
            return b_day - a_day + 1
        return sum(self.DAYS_PER_MONTH[m-1] for m in range(a_month, b_month)) - a_day + b_day + 1