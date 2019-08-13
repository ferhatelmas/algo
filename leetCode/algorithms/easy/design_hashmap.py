class MyHashMap:
    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        return self.d.get(key, -1)

    def remove(self, key: int) -> None:
        self.d.pop(key, None)
