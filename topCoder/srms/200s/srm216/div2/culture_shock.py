class CultureShock:
    def translate(self, text):
        return " ".join(map(lambda w: "ZED" if w == "ZEE" else w, text.split(" ")))
