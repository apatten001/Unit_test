import unittest
from free_throws import Students


class TestStudents(unittest.TestCase):

    def setUp(self):

        self.student_1 = Students("Arnold", "Patten", 10, 3)
        self.student_2 = Students("Jen", "Allen", 10, 2)

    def test_fullname(self):

        self.assertEqual(self.student_1.fullname(), "Arnold Patten")
        self.assertEqual(self.student_2.fullname(), "Jen Allen")

        self.student_1.first = "Jack"
        self.student_2.first = "Jill"

        self.assertEqual(self.student_1.fullname(), "Jack Patten")
        self.assertEqual(self.student_2.fullname(), "Jill Allen")

    def test_shot_percentage(self):

        self.assertEqual(self.student_1.shot_percentage(),"Arnold Patten's shooting percentage is 70%")
        self.assertEqual(self.student_2.shot_percentage(),"Jen Allen's shooting percentage is 80%")

        self.student_1.first = "Jack"
        self.student_2.first = "Jill"

        self.assertEqual(self.student_1.shot_percentage(), "Jack Patten's shooting percentage is 70%")
        self.assertEqual(self.student_2.shot_percentage(), "Jill Allen's shooting percentage is 80%")



if __name__ == "__main__":
    unittest.main()