class Weekday:
    WEEKDAY_NAMES = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value not in self.WEEKDAY_NAMES:
            raise ValueError("Invalid weekday")
        self._name = value
