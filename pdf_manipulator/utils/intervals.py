class Intervals:
    """
    A class that manipulates numeric intervals.
    """

    def __init__(
        self,
        start: int,
        end: int,
        sets: int
    ) -> None:
        self.start = start
        self.end = end
        self.interval_range = self.end - self.start + 1
        self.sets = sets

    def calc_mid(self):
        """
        Calculate the midpoint of a range.
        """
        return self.interval_range // 2

    def create_intervals(self, subinterval: bool = False) -> None:
        """
        Split some interval in chunks with predetermined number of elements.
        """
        self.intervals = []
        i = self.start
        while i <= self.end:
            interval = (i, min(i + self.sets, self.end))
            if subinterval:
                self.subintervals.append(interval)
            self.intervals.append(interval)
            i += self.sets + 1

    def create_subintervals(self) -> None:
        """
        Split each interval in half.
        """
        self.sets = self.sets // 2
        self.subintervals = []
        for interval in self.intervals:
            self.start, self.end = interval
            self.create_intervals(subinterval=True)

    def prepare_intervals(self) -> list:
        """
        Create intervals and subintervals.
        """
        self.create_intervals()
        self.create_subintervals()
        return tuple(self.subintervals)
