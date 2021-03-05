class AzimuthMonitoring:
    def getAzimuth(self, instructions):
        c = 0
        for i in instructions:
            if i == "LEFT":
                c += 270
            elif i == "RIGHT":
                c += 90
            elif i == "TURN AROUND":
                c += 180
            elif i.startswith("LEFT"):
                c -= int(i.split()[1])
            elif i.startswith("RIGHT"):
                c += int(i.split()[1])
            else:
                break
            c %= 360
        return c
