from src.classes.Weekday import Weekday
from src.classes.HourRange import HourRange


class Workday:

    def __init__(self, hour_from, hour_to, day):
        self.hour_range = HourRange(hour_from, hour_to)
        self.weekday = Weekday(day)

    @property
    def hour_range(self):
        return self._hour_range

    @hour_range.setter
    def hour_range(self, value):
        if not isinstance(value, HourRange):
            raise ValueError("hour_range must be an instance of HourRange class")
        self._hour_range = value

    @property
    def weekday(self):
        return self._weekday

    @weekday.setter
    def weekday(self, value):
        if not isinstance(value, Weekday):
            raise ValueError("weekday must be an instance of Weekday class")
        self._weekday = value