import unittest
from lab3_oop import EducationalInstitution, sort_institutions, find_institution


class TestEducationalInstitution(unittest.TestCase):

    def setUp(self):

        self.inst1 = EducationalInstitution(
            "Університет А", 4, 10000, 1900, True)
        self.inst2 = EducationalInstitution(
            "Університет Б", 4, 20000, 1850, True)
        self.inst3 = EducationalInstitution("Коледж В", 2, 1500, 1980, False)
        self.institutions = [self.inst1, self.inst2, self.inst3]

    def test_equality(self):

        identical_inst = EducationalInstitution(
            "Університет А", 4, 10000, 1900, True)
        different_inst = EducationalInstitution(
            "Університет А", 4, 10000, 1901, True)  # Різний рік

        self.assertEqual(self.inst1, identical_inst)
        self.assertNotEqual(self.inst1, different_inst)

    def test_sorting_logic(self):

        sorted_list = sort_institutions(self.institutions)

        self.assertEqual(sorted_list[0].name, "Коледж В")

        self.assertEqual(sorted_list[1].name, "Університет Б")

        self.assertEqual(sorted_list[2].name, "Університет А")

    def test_find_existing_institution(self):

        target = EducationalInstitution("Коледж В", 2, 1500, 1980, False)
        idx, obj = find_institution(self.institutions, target)

        self.assertEqual(idx, 2)
        self.assertIsNotNone(obj)

    def test_find_non_existing_institution(self):

        target = EducationalInstitution(
            "Невідомий Університет", 3, 5000, 2005, False)
        idx, obj = find_institution(self.institutions, target)

        self.assertEqual(idx, -1)
        self.assertIsNone(obj)


if __name__ == '__main__':
    unittest.main()
