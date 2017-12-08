import unittest
from employee import Employee


class TestEmploy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.emp_1 = Employee("Arnold", "Patten", 90000)
        self.emp_2 = Employee("Jen", "Patten", 100000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "ArnoldPatten@company.com")
        self.assertEqual(self.emp_2.email, "JenPatten@company.com")

        self.emp_1.first = "Jack"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "JackPatten@company.com")
        self.assertEqual(self.emp_2.email, "JanePatten@company.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1, "Arnold Patten")
        self.assertEqual(self.emp_2, "Jen Patten")

        self.emp_1.first = "Jack"
        self.emp_2.first = "Jill"

        self.assertEqual(self.emp_1, "Jack Patten")
        self.assertEqual(self.emp_2, "Jill Patten")

    def test_apply_raise(self):
        self.assertEqual(self.emp_1.apply_raise, 94500)
        self.assertEqual(self.emp_2.apply_raise, 105000)


if __name__ == "__main__":
    unittest.main()
