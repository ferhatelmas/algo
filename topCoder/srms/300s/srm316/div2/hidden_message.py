class HiddenMessage:
    def getMessage(self, text):
        return "".join(map(lambda e: e[:1], text.split()))
