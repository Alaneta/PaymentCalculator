import re


def is_valid_time(value):
    reg = re.compile(r'(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]')
    return reg.search(value)


class HourRange:
    def __init__(self, hour_from, hour_to):
        self.hour_from = hour_from
        self.hour_to = hour_to

    @property
    def hour_from(self):
        return self._hour_from

    @hour_from.setter
    def hour_from(self, value):
        if not is_valid_time(value):
            raise ValueError("Incorrect data format, should be HH-MM")
        self._hour_from = value

    @property
    def hour_to(self):
        return self._hour_to

    @hour_to.setter
    def hour_to(self, value):
        if not is_valid_time(value):
            raise ValueError("Incorrect data format, should be HH-MM")
        self._hour_to = value