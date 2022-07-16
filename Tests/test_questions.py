import unittest
from Source import questions


class TestOldExam(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(TypeError):
            questions.OldExamModel("AFA", "2o21")

        self.assertIsInstance(questions.OldExamModel("ENEM", 2016), questions.OldExamModel)


class TestQuestionID(unittest.TestCase):
    def test_check_existence(self):
        with self.assertRaises(TimeoutError):
            questions.QuestionID(desired_id="testing", parent_dir="CursoFull/Registry")

        self.assertEqual(questions.QuestionID(parent_dir="CursoFull/Registry").check_if_id_exists(master_filepath="CursoFull/Registry/question_statistics.csv", new_id="testing"), True)


class TestHTMLString(unittest.TestCase):
    def test_add_tags(self):
        self.assertEqual(questions.HTMLString("testing").__str__(), "<span>testing</span>")


class TestAlternativeModel(unittest.TestCase):
    def test_available_answer(self):
        with self.assertRaises(ValueError):
            questions.AlternativeModel(A=1, B=2, C=3, D=4, answer="E")
        with self.assertRaises(TypeError):
            questions.AlternativeModel(A=1, B=2, C=3, D=4, answer=None)
        with self.assertRaises(TypeError):
            questions.AlternativeModel(A=1, B=2, C=3, D=4, answer=-1)

    def test_provided_alternatives(self):
        pass


if __name__ == '__main__':
    unittest.main()
