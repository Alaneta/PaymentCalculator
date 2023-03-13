from datetime import datetime
from src.classes.Workday import Workday
from src.constants import PAYMENT_VALUES


class PaymentCalculator:

    def __init__(self, workday):
        self.workday = workday

    @property
    def workday(self):
        return self._workday

    @workday.setter
    def workday(self, value):
        if not isinstance(value, Workday):
            raise ValueError("workday must be an instance of Workday class")
        self._workday = value

    def get_amount_to_paid(self):
        hour_from = self.workday.hour_range.hour_from
        hour_to = self.workday.hour_range.hour_to
        daily_total_amount = 0
        for schedule in PAYMENT_VALUES[self.workday.weekday.name]:
            sch_hour_to_24 = schedule['hour_to'].replace('00:00', '24:00')
            hour_to_24 = hour_to.replace('00:00', '24:00')
            if schedule['hour_from'] <= hour_from <= sch_hour_to_24 and hour_to_24 <= sch_hour_to_24:
                worked_hours = (datetime.strptime(hour_to, "%H:%M") - datetime.strptime(hour_from, "%H:%M")).seconds/3600
                daily_total_amount += schedule['amount'] * worked_hours
                return daily_total_amount
            if schedule['hour_from'] <= hour_from < sch_hour_to_24 < hour_to_24:
                worked_hours = (datetime.strptime(schedule['hour_to'], "%H:%M") - datetime.strptime(hour_from, "%H:%M")).seconds/3600
                daily_total_amount += schedule['amount'] * worked_hours
                hour_from = schedule['hour_to']
        raise ValueError(
            "There is no payment data for this specific workday: " + self.workday.weekday.name + ' ' + hour_from + '-' + hour_to)