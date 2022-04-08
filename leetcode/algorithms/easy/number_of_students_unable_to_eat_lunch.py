from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one = students.count(1)
        zero = len(students) - one
        for i, e in enumerate(sandwiches):
            if e == 1:
                one -= 1
            else:
                zero -= 1

            if one < 0 or zero < 0:
                return len(sandwiches) - i
        return 0
