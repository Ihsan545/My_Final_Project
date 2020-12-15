import unittest
from final_project.employee_class import Employee

"""Test file for employee_class.py"""


def test_all_attributes():
    employee = Employee('Mike', 'John', 5, 'Management', 'Manager', '4000',
                        '01-04-2014')
    assert employee == 'Mike'
    assert employee == 'John'


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Mike', 'John', 5, 'Management', 'Manager', '4000', '01-04-2014')

    def tearDown(self):
        del self.employee

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.employee, 'Mike')
        self.assertEqual(self.employee, 'John')

    def test_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = Employee('444', 'John', 5, 'Management', 'Manager', '4000', '01-04-2014')

    def test_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = Employee('Mike', '333', 5, 'Management', 'Manager', '4000', '01-04-2014')


if __name__ == '__main__':
    unittest.main()
