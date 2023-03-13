import unittest
from unittest.mock import patch, Mock
from src.classes.PaymentCalculator import PaymentCalculator


@patch('src.classes.PaymentCalculator.PAYMENT_VALUES', {
    'MO': [
        {'hour_from': '00:00', 'hour_to': '09:00', 'amount': 25},
        {'hour_from': '09:00', 'hour_to': '18:00', 'amount': 15}
    ]
})
class TestPaymentCalculator(unittest.TestCase):

    # Tests calculation when having a work hour range that includes only one payment value per hour
    def test_get_amount_to_paid_simple(self):
        with patch.object(PaymentCalculator, 'workday') as mock_workday:
            hour_range_mock = Mock()
            weekday_mock = Mock()
            hour_range_mock.hour_from = '09:00'
            hour_range_mock.hour_to = '18:00'
            weekday_mock.name = 'MO'
            workday_mock = Mock(hour_range=hour_range_mock, weekday=weekday_mock)
            mock_workday.return_value = workday_mock

            payment_calculator = PaymentCalculator(workday_mock)
            amount_to_paid = payment_calculator.get_amount_to_paid()

            self.assertEqual(amount_to_paid, 135)

    # Tests calculation when having a work hour range that includes more than one payment value per hour
    def test_get_amount_to_paid_advanced(self):
        with patch.object(PaymentCalculator, 'workday') as mock_workday:
            hour_range_mock = Mock()
            weekday_mock = Mock()
            hour_range_mock.hour_from = '05:00'
            hour_range_mock.hour_to = '15:00'
            weekday_mock.name = 'MO'
            workday_mock = Mock(hour_range=hour_range_mock, weekday=weekday_mock)
            mock_workday.return_value = workday_mock

            payment_calculator = PaymentCalculator(workday_mock)
            amount_to_paid = payment_calculator.get_amount_to_paid()

            self.assertEqual(amount_to_paid, 190)

    # Checks that method returns error if work hour range is out of margin
    def test_get_amount_to_paid_error(self):
        with patch.object(PaymentCalculator, 'workday') as mock_workday:
            hour_range_mock = Mock()
            weekday_mock = Mock()
            hour_range_mock.hour_from = '18:00'
            hour_range_mock.hour_to = '22:00'
            weekday_mock.name = 'MO'
            workday_mock = Mock(hour_range=hour_range_mock, weekday=weekday_mock)
            mock_workday.return_value = workday_mock

            payment_calculator = PaymentCalculator(workday_mock)
            with self.assertRaises(ValueError):
                payment_calculator.get_amount_to_paid()
