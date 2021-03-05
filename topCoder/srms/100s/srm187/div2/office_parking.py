class OfficeParking:
    def spacesUsed(self, events):
        park = []
        for e in events:
            w, a = e.split()
            if a == "arrives":
                if -1 in park:
                    park[park.index(-1)] = w
                else:
                    park.append(w)
            else:
                park[park.index(w)] = -1
        return len(park)
