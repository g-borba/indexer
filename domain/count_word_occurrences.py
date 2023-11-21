from os import curdir
from re import findall
from collections import defaultdict
from models.word_statistics import WordStatistics


class CountWordOcurrences:
    def __init__(self, file_name: str) -> None:
        self.path = f"{curdir}/assets/{file_name}.txt"

        self.word_statistics = defaultdict(WordStatistics)

    def count_occurrences(self, target_word: str) -> None:
        with open(self.path, "r", encoding="utf-8", errors="replace") as file:
            for line in file:
                words = findall(r"\b\w+\b", line.lower())
                for word in words:
                    if target_word == word:
                        self.word_statistics[word].add_occurrence(word)

        print(*(self.word_statistics).values())
