import unittest
import datetime
import payment_calculator as pc


class TestCases(unittest.TestCase):
    def test_string_to_date_parser(self):
        self.assertEqual(pc.split_time_string("11:00-20:00"),
                         (datetime.datetime.strptime("11:00", '%H:%M').time(),
                          datetime.datetime.strptime("20:00", '%H:%M').time()))

    def test_salary_range1(self):
        self.assertEqual(pc.calculate_hour_worked_price("1:00-03:00")[0], 25)

    def test_salary_range2(self):
        self.assertEqual(pc.calculate_hour_worked_price("10:00-12:00")[0], 15)

    def test_salary_range3(self):
        self.assertEqual(pc.calculate_hour_worked_price("20:00-21:00")[0], 20)

    def test_worked_hours_calculation(self):
        self.assertEqual(pc.calculate_hour_worked_price("10:00-12:00")[1], 2)


if __name__ == '__main__':
    unittest.main()
