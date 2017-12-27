import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("Arnold".upper(), "ARNOLD")

    def test_lower(self):
        self.assertEqual("ARNOLD".lower(),"arnold")

    def test_capitalize(self):
        self.assertEqual("jennifer".capitalize(),"Jennifer")

    def test_greater(self):
        self.assertGreater(7,4)

    def test_is_not(self):
        self.assertIsNot("I left Home", "I left home")

    def test_is(self):
        self.assertIs("I left Home", "I left Home")













if __name__ == "__main__":
    unittest.main()