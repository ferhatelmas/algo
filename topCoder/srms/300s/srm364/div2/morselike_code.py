class MorselikeCode:
    def decrypt(self, library, message):
        d = dict(e.split()[::-1] for e in library)
        return "".join(d.get(e, "?") for e in message.split())
