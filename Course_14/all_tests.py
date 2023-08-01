import unittest

test_loader = unittest.TestLoader()
another_suite = test_loader.loadTestsFromNames(["employee_tests", "math_tests"])
unittest.TextTestRunner().run(another_suite)
