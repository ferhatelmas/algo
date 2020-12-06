class Solution:
    def interpret(self, command: str) -> str:
        d = {
            "G": "G",
            "()": "o",
            "(al)": "al",
        }
        for k, v in d.items():
            command = command.replace(k, v)
        return command
