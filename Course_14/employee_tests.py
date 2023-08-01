import unittest
from unittest.mock import patch
import json
from main import Employee


class EmployeeTests(unittest.TestCase):
    employee = None

    @classmethod
    def setUpClass(cls) -> None:
        print("This is ran before all the tests")

    @classmethod
    def tearDownClass(cls) -> None:
        print("This is ran after all the tests")

    def setUp(self) -> None:
        self.employee = Employee()
        print("Employee reset")

    def tearDown(self) -> None:
        self.employee.salary = 0
        print("Salary reset")

    def test_net_salary_big_value(self):
        # Arrange
        self.employee.salary = 1000
        # Act
        result = self.employee.net_salary()
        # Assert
        self.assertEqual(550, result, "The net salary is not computed correctly")

    def test_net_salary_small_value(self):
        self.employee.salary = 10
        result = self.employee.net_salary()
        self.assertEqual(5.5, result, "The net salary is not computed correctly")

    def test_net_salary_negative_value(self):
        self.employee.salary = -10
        with self.assertRaises(ValueError):
            self.employee.net_salary()

    def test_employee_data(self):
        with patch("requests.get") as mocked_get:
            random_data = {"results": [{"name": {"first": "John", "last": "Smith"}}]}
            mocked_get.return_value.text = json.dumps(random_data)

            with patch("random.randint") as mocked_random:
                mocked_random.return_value = 5000

                self.employee.get_placeholder()
                self.assertEqual("John Smith", self.employee.name)
                self.assertEqual(self.employee.salary, 5000)
                mocked_random.assert_called_with(1000, 10_000)


if __name__ == "__main__":
    unittest.main()
