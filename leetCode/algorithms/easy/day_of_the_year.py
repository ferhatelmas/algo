from datetime import datetime


class Solution:
    def dayOfYear(self, date: str) -> int:
        d = datetime.strptime(date, "%Y-%m-%d")
        return (d - d.replace(month=1, day=1)).days + 1
