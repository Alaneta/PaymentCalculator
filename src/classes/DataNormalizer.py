import re
from src.constants import NAME_DELIMITER, WORKDAY_DELIMITER, HOUR_RANGE_DELIMITER


def is_valid_entry(value):
    matches = re.match('\w+=(\w\w\d\d:\d\d-\d\d:\d\d,*)+(\w\w\d\d:\d\d-\d\d:\d\d)*', value)
    return matches and matches[0] == value


class DataNormalizer:

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        value = value.strip()
        if not is_valid_entry(value):
            raise ValueError('Invalid entry format. Entry format must be of type "{NAME}={DAY}{HH:MM}-{HH:MM},..."')
        self._data = value

    def normalize(self):
        delimiter_pos = self.data.find(NAME_DELIMITER)
        employee_name = self.data[0:delimiter_pos]
        workdays = self.data[delimiter_pos + 1:len(self.data)].split(WORKDAY_DELIMITER)
        workdays = map(lambda x: {'weekday': x[0:2], 'hour_range': x[2:len(x)].split(HOUR_RANGE_DELIMITER)}, workdays)
        return {
            'employee_name': employee_name,
            'workdays': list(workdays)
        }