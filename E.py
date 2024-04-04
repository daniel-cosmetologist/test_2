#############################

# E. Класс для анализа текста

#############################

import functools
import time

def time_measure(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Метод {func.__name__!r} выполнен за {end_time - start_time:.4f} сек.")
        return result
    return wrapper

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.words = [word.strip(".,!?:;()\"") for word in text.split()]
        self.special_chars = ".,!?:;()\""

    @time_measure
    def longest_word(self):
        print(max(self.words, key=len))

    @time_measure
    def most_common_word(self):
        print(max(set(self.words), key=self.words.count))

    @time_measure
    def special_characters_count(self):
        print(sum(1 for char in self.text if char in self.special_chars))

    @time_measure
    def palindromes(self):
        palindromes = [word for word in self.words if word == word[::-1] and len(word) > 1]
        print(','.join(palindromes))

def run_text_analyzer():
    text = "In computing, plain text is a loose term for data (e.g. file contents) that represent only characters of readable material but not its graphical representation nor other objects (floating-point numbers, images, etc.). It may also include a limited number of whitespace characters that affect simple arrangement of text, such as spaces, line breaks, or tabulation characters. Palidrome examples: civic, radar, level, rotor, kayak, madam, and refer"
    analyzer = TextAnalyzer(text)
    analyzer.longest_word()
    analyzer.most_common_word()
    analyzer.special_characters_count()
    analyzer.palindromes()

if __name__ == "__main__":
    run_text_analyzer()
