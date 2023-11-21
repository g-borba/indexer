from os import curdir
from re import findall
from math import log
from collections import defaultdict
from models.word_statistics import WordStatistics


class SearchRelevantFilesByTerms:
    def __init__(self, file_names: str) -> None:
        self.paths = [f"{curdir}/assets/{file_name}.txt" for file_name in file_names]

        self.word_statistics = defaultdict(WordStatistics)
        self.word_document_count = defaultdict(int)

    def calculate_tfidf(self):
        document_count = len(self.paths)

        for key in self.word_document_count.keys():
            idf = log(document_count / self.word_document_count[key], 2)
            self.word_document_count[key] = idf

        for key in self.word_statistics.keys():
            self.word_statistics[key].set_tfidf(idf=self.word_document_count[key[1]], key=key)

        print(*self.word_statistics.values())

    def list_relevant_files(self, terms: str) -> None:
        term_list = terms[0].split()

        for path in self.paths:
            with open(path, "r", encoding="ascii", errors="replace") as file:
                total = 0
                found_words = {}

                for line in file:
                    words = findall(r"\b[A-Za-z]{2,}\b", line.lower())

                    for word in words:
                        if word in term_list:
                            found_words[word] = 1
                            key = (path, word)
                            self.word_statistics[key].add_occurrence(key)
                        total += 1

                for word in found_words.keys():
                    key = (path, word)
                    self.word_document_count[word] += 1
                    self.word_statistics[key].calculate_frequency(total, key)

        self.calculate_tfidf()
