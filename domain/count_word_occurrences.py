from os import curdir
from re import escape, compile, IGNORECASE
from collections import defaultdict
from models.word_statistics import WordStatistics


class CountWordOcurrences:
    def __init__(self, file_name: str) -> None:
        self.path = f"{curdir}/assets/{file_name}.txt"

        self.word_statistics = defaultdict(WordStatistics)

    def count_occurrences(self, target_word: str) -> None:
        with open(self.path, "r", encoding="utf-8", errors="replace") as file:
            escaped_target_word = escape(target_word)
            pattern = compile(rf"\b{escaped_target_word}\b", IGNORECASE)

            for line in file:
                matches = pattern.findall(line)
                for _ in range(len(matches)):
                    self.word_statistics[target_word].add_occurrence(target_word)

        print(*(self.word_statistics).values())
