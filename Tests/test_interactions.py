import unittest
from Source import interactions as inter


class TestInteractions(unittest.TestCase):
    def test_random_question(self):
        interactions = inter.Interactions(parent_dir="../Registry")

        with self.assertRaises(LookupError):
            interactions.get_random_question_from_parameters(discipline="NONEXISTENT")

        with self.assertRaises(TypeError):
            interactions.get_random_question_from_parameters(discipline=None)

        self.assertEqual(interactions.get_random_question_from_parameters(discipline="TESTING"), "testing")


if __name__ == '__main__':
    unittest.main()
