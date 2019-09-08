from datetime import date


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
        return days[(date(year, month, day).weekday() + 1) % len(days)]
