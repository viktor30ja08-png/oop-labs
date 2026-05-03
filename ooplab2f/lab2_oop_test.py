import unittest
from lab2_oop import is_vowel, count_vowels, extract_words, sort_words_by_vowels


class TestStringOperations(unittest.TestCase):

    def test_is_vowel(self):
        """Перевірка розпізнавання голосних"""
        self.assertTrue(is_vowel('а'))
        self.assertTrue(is_vowel('E'))
        self.assertFalse(is_vowel('б'))
        self.assertFalse(is_vowel('z'))
        self.assertFalse(is_vowel('1'))
        self.assertFalse(is_vowel(' '))

    def test_count_vowels(self):
        """Перевірка підрахунку голосних у слові"""
        word1 = list("Привіт")  # и, і (2)
        word2 = list("Студент")  # у, е (2)
        word3 = list("Текст")   # е (1)
        word4 = list("Врт")     # (0)

        self.assertEqual(count_vowels(word1), 2)
        self.assertEqual(count_vowels(word2), 2)
        self.assertEqual(count_vowels(word3), 1)
        self.assertEqual(count_vowels(word4), 0)

    def test_extract_words(self):
        """Перевірка ручного виділення слів (без split)"""
        text = list("Привіт, світе! Як справи?")
        expected = [list("Привіт"), list("світе"), list("Як"), list("справи")]
        self.assertEqual(extract_words(text), expected)

    def test_empty_text(self):
        """Перевірка обробки тексту без літер"""
        self.assertEqual(extract_words(list("   , . ! ")), [])

    def test_sort_words_by_vowels(self):
        """Перевірка правильності сортування слів"""
        words = [list("ааа"), list("б"), list("а")]
        expected = [list("б"), list("а"), list("ааа")]

        self.assertEqual(sort_words_by_vowels(words), expected)


if __name__ == '__main__':
    unittest.main()
