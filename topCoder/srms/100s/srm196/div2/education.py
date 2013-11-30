class Education:
    def minimize(self, desire, tests):
        req = (90 - (ord(desire) - ord('A')) * 10) * (len(tests)+1) - sum(tests)
        if req > 100:
            return -1
        elif req < 0:
            return 0
        return req
