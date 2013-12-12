class ColorCode:
    def getOhms(self, code):
        d = {
            'black': ('0', 1),
            'brown': ('1', 10),
            'red': ('2', 100),
            'orange': ('3', 1000),
            'yellow': ('4', 10000),
            'green': ('5', 100000),
            'blue': ('6', 1000000),
            'violet': ('7', 10000,000),
            'grey': ('8', 100000000),
            'white': ('9', 1000000000)
        }
        return int(d[code[0]][0] + d[code[1]][0]) * d[code[2]][1]
