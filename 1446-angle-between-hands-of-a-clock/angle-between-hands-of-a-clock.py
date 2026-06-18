class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr_angle = (hour % 12 + (minutes / 60)) / 12 * 360
        min_angle = minutes / 60 * 360
        # print('hr_angle', hr_angle, 'min_angle', min_angle)
        abs_diff = max(hr_angle, min_angle) - min(hr_angle, min_angle)
        # print('abs_diff', abs_diff)
        return abs_diff if abs_diff <= 180 else 360 - abs_diff