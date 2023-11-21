from collections import defaultdict


class WordStatistics:
    def __init__(self):
        self.word_occurrences = defaultdict(int)

    def add_occurrence(self, word):
        self.word_occurrences[word] += 1

    def calculate_frequency(self, total, key):
        count = self.word_occurrences[key]
        self.word_occurrences[key] = count / total

    def set_tfidf(self, idf, key):
        tf = self.word_occurrences[key]
        self.word_occurrences[key] = tf * idf

    def __repr__(self):
        return f"{dict(self.word_occurrences)}"
