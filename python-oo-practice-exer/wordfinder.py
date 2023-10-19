"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:

    def __init__(self, file_path):
        self.file_path = file_path
        self.words_list = self.read_file()
        print(f"{len(self.words_list)} words read")

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:  # open file in read mode variable name: file
                content = file.read()  # reads entire content of file
                words_list = content.split('\n')
                words_list = [word for word in words_list if word]
                return words_list

        except FileNotFoundError:
            return []

    def random(self):
        random_word = random.choice(self.words_list)
        return random_word


class SpecialWordFinder(WordFinder):

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                words_list = content.split('\n')
                words_list = [
                    word for word in words_list if word.strip() and not word.startswith('#')]
                return words_list
        except FileNotFoundError:
            return []
