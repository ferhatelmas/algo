class Chivalry:
    def getOrder(self, first, second):
        last = []
        while first or second:
            if first and not second:
                last.append(first)
                first = ""
            elif not first and second:
                last.append(second)
                second = ""
            elif first[0] == second[0] or first[0] == "W":
                last.append(first[0])
                first = first[1:]
            else:
                last.append(second[0])
                second = second[1:]
        return "".join(last)
