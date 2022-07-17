import unittest
from Source import disciplines


# TODO: ADD ALL TESTS
class TestDisciplines(unittest.TestCase):
    def test_get_discipline_names(self):
        self.assertEqual(disciplines.get_all_discipline_names()[0],"INGLÊS")

    def test_get_all_areas(self):
        _expected = ['COMPREENSÃO E INTERPRETAÇÃO DE TEXTOS', 'ESTRUTURAS GRAMATICAIS']
        self.assertEqual(disciplines.get_all_areas_from_discipline("INGLÊS"), _expected)
        self.assertEqual(disciplines.get_all_areas_from_discipline("inglês"), _expected)

        with self.assertRaises(KeyError):
            disciplines.get_all_areas_from_discipline("Testing")

    def test_get_all_subjects(self):
        _expected = ["Introdução à termologia", "Termometria", "Dilatação térmica de sólidos e líquidos"]
        self.assertEqual(disciplines.get_all_subjects_from_area("FÍSICA","TERMOLOGIA"), _expected)
        self.assertEqual(disciplines.get_all_subjects_from_area("FÍSICA","termologia"), _expected)

        with self.assertRaises(KeyError):
            disciplines.get_all_subjects_from_area("TESTING", "TESTING")

        with self.assertRaises(KeyError):
            disciplines.get_all_subjects_from_area("MATEMÁTICA", "TESTING")


if __name__ == '__main__':
    unittest.main()
