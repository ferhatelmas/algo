class grafixClick:
    def checkSaveButton(self, mouseRows, mouseCols):
        return filter(
            lambda i: i is not None,
            map(
                lambda (i, (r, c)): i if (20 <= r <= 39) and (50 <= c <= 99) else None,
                enumerate(zip(mouseRows, mouseCols)),
            ),
        )
