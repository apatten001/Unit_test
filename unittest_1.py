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

    def test_append(self):
        a = ["Arnold"]
        a.append("Jennifer")
        self.assertEqual(a, ["Arnold", "Jennifer"])

    def test_remove(self):
        b = ["Arnold", "Jennifer"]
        b.remove("Arnold")
        self.assertEqual(b,["Jennifer"])

    def test_split(self):
        c  = "Arnold Jen Rob Chris"
        self.assertEqual(c.split(" "), ["Arnold", "Jen", "Rob", "Chris"])












if __name__ == "__main__":
    unittest.main()