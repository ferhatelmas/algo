from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, stack = set(), [0]
        while stack:
            room = stack.pop()
            visited.add(room)

            stack += [r for r in rooms[room] if r not in visited]

        return len(visited) == len(rooms)
