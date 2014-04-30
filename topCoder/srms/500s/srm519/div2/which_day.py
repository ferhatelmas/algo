class WhichDay:
    def getDay(self, notOnThisDay):
        for d in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"):
            if d not in notOnThisDay:
                return d
