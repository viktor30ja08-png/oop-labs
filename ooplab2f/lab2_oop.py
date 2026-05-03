def is_vowel(char):
    vowels = "аеєиіїоуюяaeiouyАЕЄИІЇОУЮЯAEIOUY"
    return char in vowels


def count_vowels(word_chars):

    count = 0
    for char in word_chars:
        if is_vowel(char):
            count += 1
    return count


def extract_words(text_chars):

    words = []
    current_word = []

    for char in text_chars:
        if char.isalpha():
            current_word.append(char)
        elif current_word:
            words.append(current_word)
            current_word = []

    if current_word:
        words.append(current_word)

    return words


def sort_words_by_vowels(words):

    n = len(words)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if count_vowels(words[j]) > count_vowels(words[j + 1]):
                # Міняємо місцями
                words[j], words[j + 1] = words[j + 1], words[j]
    return words


def main():
    try:
        # 1. Введення даних (імітація перетворення String -> StringBuffer)
        original_text = "Це тестовий рядок для лабораторної роботи. Студент вивчає програмування!"
        print(f"Початковий текст:\n{original_text}\n")

        # Перетворюємо рядок на список символів для мутабельності
        text_buffer = list(original_text)

        # 2. Виділення слів
        words_buffer = extract_words(text_buffer)

        if not words_buffer:
            raise ValueError("Текст не містить жодного слова.")

        # 3. Сортування слів
        sorted_words_buffer = sort_words_by_vowels(words_buffer)

        # 4. Виведення результату (імітація перетворення StringBuffer -> String)
        print("Слова, відсортовані за зростанням кількості голосних літер:")
        for word_chars in sorted_words_buffer:
            # Збираємо символи назад у слово для виведення
            word_str = "".join(word_chars)
            vowels_count = count_vowels(word_chars)
            print(f"{word_str} (голосних: {vowels_count})")

    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
