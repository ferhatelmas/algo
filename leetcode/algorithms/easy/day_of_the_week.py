from datetime import date


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = [
            "",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        return days[date(year, month, day).isoweekday()]
