import unittest
from Source import interactions as inter


class TestInteractions(unittest.TestCase):
    def test_random_question(self):
        interactions = inter.Interactions(parent_dir="../Registry")

        with self.assertRaises(LookupError):
            interactions.get_random_question_from_parameters(discipline="NONEXISTENT")
        with self.assertRaises(LookupError):
            interactions.get_random_question_from_parameters(discipline="MATEMÁTICA", area="NONEXISTENT")

        with self.assertRaises(TypeError):
            interactions.get_random_question_from_parameters(discipline=3)
        with self.assertRaises(TypeError):
            interactions.get_random_question_from_parameters(discipline=None)

        self.assertEqual(interactions.get_random_question_from_parameters(discipline="TESTING"), "testing")

        with self.assertRaises(LookupError):
            interactions.get_random_question_from_parameters(discipline="TESTING", difficulty_level=(0,2))
        with self.assertRaises(LookupError):
            interactions.get_random_question_from_parameters(discipline="TESTING", difficulty_level=(4,2))

        self.assertEqual(
            interactions.get_random_question_from_parameters(discipline="TESTING", difficulty_level=(0,3)), "testing")
        self.assertEqual(
            interactions.get_random_question_from_parameters(discipline="TESTING", difficulty_level=(0, 10)), "testing")

        with self.assertRaises(TypeError):
            interactions.get_random_question_from_parameters(discipline="TESTING", difficulty_level="one")


if __name__ == '__main__':
    unittest.main()
