import unittest
from Source import questions


# TODO: ADJUST SYS PATHS, IT DOESN'T WORK LIKE THIS
class TestOldExam(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(ValueError):
            questions.OldExamModel("AFA", "2o21")

        self.assertIsInstance(questions.OldExamModel("ENEM", 2016), questions.OldExamModel)


if __name__ == '__main__':
    unittest.main()
