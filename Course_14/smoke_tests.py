import unittest
import math_tests
import employee_tests

test_suite = unittest.TestSuite()
test_suite.addTest(employee_tests.EmployeeTests("test_net_salary_big_value"))
test_suite.addTest(math_tests.MathTests("test_division"))
unittest.TextTestRunner().run(test_suite)
