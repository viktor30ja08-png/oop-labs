import unittest
from lab4_oop import Letter, Word, Punctuation, Sentence, Text, sort_words_bubble


class TestTextOOP(unittest.TestCase):

    def test_letter_vowel(self):
        self.assertTrue(Letter("A").is_vowel())
        self.assertTrue(Letter("e").is_vowel())
        self.assertFalse(Letter("z").is_vowel())
        self.assertFalse(Letter("B").is_vowel())

    def test_word_vowel_count(self):
        word1 = Word("Queue")
        word2 = Word("Crypt")
        self.assertEqual(word1.count_vowels(), 4)
        self.assertEqual(word2.count_vowels(), 1)

    def test_text_cleaning(self):
        text = Text("Space \t\t and    tabs.")
        expected_str = "Space and tabs."
        self.assertEqual(str(text), expected_str)

    def test_extract_words(self):
        sentence = Sentence("Hello, world!")
        words = sentence.get_words()
        self.assertEqual(len(words), 2)
        self.assertEqual(str(words[0]), "Hello")
        self.assertEqual(str(words[1]), "world")

    def test_bubble_sort(self):
        w1 = Word("Apple")  # 2 vowels
        w2 = Word("Dog")    # 1 vowel
        w3 = Word("Queue")  # 4 vowels
        w4 = Word("Fly")    # 1 vowel

        words_list = [w1, w2, w3, w4]
        sorted_list = sort_words_bubble(words_list)

        self.assertEqual(sorted_list[0].count_vowels(), 1)
        self.assertEqual(sorted_list[1].count_vowels(), 1)
        self.assertEqual(sorted_list[2].count_vowels(), 2)
        self.assertEqual(sorted_list[3].count_vowels(), 4)


if __name__ == "__main__":
    unittest.main()
