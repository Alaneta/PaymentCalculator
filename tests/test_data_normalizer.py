import unittest
from unittest.mock import patch
from src.classes.DataNormalizer import is_valid_entry, DataNormalizer


@patch('src.classes.DataNormalizer.NAME_DELIMITER', '=')
@patch('src.classes.DataNormalizer.WORKDAY_DELIMITER', ',')
@patch('src.classes.DataNormalizer.HOUR_RANGE_DELIMITER', '-')
class TestDataNormalizer(unittest.TestCase):

    # Checks if method returns true when having a valid entry
    def test_is_valid_entry(self):
        value = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        self.assertTrue(is_valid_entry(value))

    # Checks if method returns false when having a valid entry
    def test_is_not_valid_entry(self):
        value = 'RENEMO10:00-12:00'
        self.assertFalse(is_valid_entry(value))

    # Checks data result when having a valid data entry
    def test_normalize(self):
        with patch.object(DataNormalizer, 'data') as mock_data:
            data = 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
            mock_data.return_value = data

            normalizer = DataNormalizer(data)
            self.assertEqual(normalizer.normalize(), {
                'employee_name': 'ASTRID',
                'workdays': [
                    {
                        'weekday': 'MO',
                        'hour_range': ['10:00', '12:00']
                    },
                    {
                        'weekday': 'TH',
                        'hour_range': ['12:00', '14:00']
                    },
                    {
                        'weekday': 'SU',
                        'hour_range': ['20:00', '21:00']
                    }
                ]
            })