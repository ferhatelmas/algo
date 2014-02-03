class ToolsBox:
    def countTools(self, need):
        s = set()
        for e in need:
            s.update(e.split())
        return len(s)
