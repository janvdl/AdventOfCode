class Disc:
    def __init__(self, numpos, startpos):
        self.numpos = numpos
        self.startpos = startpos

    def pos_at_time(self, time):
        return (self.startpos + time) % self.numpos