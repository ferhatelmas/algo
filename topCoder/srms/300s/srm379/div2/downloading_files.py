class DownloadingFiles:
    def actualTime(self, tasks):
        b, w = 0, 0.0
        for e in tasks:
            bw, t = map(int, e.split())
            b += bw
            w += bw * t
        return w / b
