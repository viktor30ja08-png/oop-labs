class Letter:
    def __init__(self, char):
        self.char = char

    def is_vowel(self):
        vowels = "aeiouyAEIOUY"
        return self.char in vowels

    def __str__(self):
        return self.char


class Word:
    def __init__(self, word_str):
        self.letters = []
        for char in word_str:
            self.letters.append(Letter(char))

    def count_vowels(self):
        count = 0
        for letter in self.letters:
            if letter.is_vowel():
                count += 1
        return count

    def __str__(self):
        result = ""
        for letter in self.letters:
            result += str(letter)
        return result


class Punctuation:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char


class Sentence:
    def __init__(self, sentence_str):
        self.elements = []
        word_chars = ""

        for char in sentence_str:
            if char.isalpha():
                word_chars += char
            else:
                if word_chars != "":
                    self.elements.append(Word(word_chars))
                    word_chars = ""
                if char != " ":
                    self.elements.append(Punctuation(char))

        if word_chars != "":
            self.elements.append(Word(word_chars))

    def get_words(self):
        words = []
        for element in self.elements:
            if isinstance(element, Word):
                words.append(element)
        return words

    def __str__(self):
        result = ""
        for element in self.elements:
            if isinstance(element, Word):
                if result != "" and not result.endswith(" "):
                    result += " "
                result += str(element)
            else:
                result += str(element)
        return result.strip()


class Text:
    def __init__(self, text_str):
        cleaned_text = self.remove_extra_spaces(text_str)
        self.sentences = []
        sentence_chars = ""

        for char in cleaned_text:
            sentence_chars += char
            if char in ".!?":
                self.sentences.append(Sentence(sentence_chars.strip()))
                sentence_chars = ""

        if sentence_chars.strip() != "":
            self.sentences.append(Sentence(sentence_chars.strip()))

    def remove_extra_spaces(self, text_str):
        cleaned = ""
        space_found = False
        for char in text_str:
            if char == " " or char == "\t":
                if not space_found:
                    cleaned += " "
                    space_found = True
            else:
                cleaned += char
                space_found = False
        return cleaned.strip()

    def get_all_words(self):
        words = []
        for sentence in self.sentences:
            for word in sentence.get_words():
                words.append(word)
        return words

    def __str__(self):
        result = ""
        for sentence in self.sentences:
            result += str(sentence) + " "
        return result.strip()


def sort_words_bubble(words):
    n = len(words)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if words[j].count_vowels() > words[j + 1].count_vowels():
                temp = words[j]
                words[j] = words[j + 1]
                words[j + 1] = temp
    return words


def main():
    input_data = "This    text   has \t\t multiple spaces. And it has some words!"

    print("Original Input:")
    print(input_data)

    text_object = Text(input_data)

    all_words = text_object.get_all_words()
    sorted_words = sort_words_bubble(all_words)

    print("Words sorted by vowel count (ascending):")
    for word in sorted_words:
        print(str(word) + " (vowels: " + str(word.count_vowels()) + ")")


if __name__ == "__main__":
    main()
