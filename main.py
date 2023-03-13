import logging
import traceback
from src.classes.Workday import Workday
from src.classes.DataNormalizer import DataNormalizer
from src.classes.PaymentCalculator import PaymentCalculator

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    try:
        logger.info("BEGIN: Process started")
        with open('entries.txt') as f:
            entries = f.readlines()
            for entry in entries:
                normalized_data = DataNormalizer(entry).normalize()
                total_amount = 0
                for workday in normalized_data['workdays']:
                    workday = Workday(workday['hour_range'][0], workday['hour_range'][1], workday['weekday'])
                    payment_calculator = PaymentCalculator(workday)
                    total_amount += payment_calculator.get_amount_to_paid()
                print('The amount to pay ' + normalized_data['employee_name'] + ' is: ' + str(round(total_amount, 2)) + ' USD')
        logger.info("END: Process finished")
    except:
        logger.error(str(traceback.format_exc()))