class CssPropertyConverter:
    def getCamelized(self, cssPropertyName):
        cs = cssPropertyName.split("-")
        return "".join(cs[:1] + map(lambda e: e.capitalize(), cs[1:]))
