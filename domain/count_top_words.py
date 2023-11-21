from os import curdir
from re import findall
from models.binary_tree import BinarySearchTree


class CountTopWords:
    def __init__(self, file_name: str) -> None:
        self.path = f"{curdir}/assets/{file_name}.txt"

        self.bst = BinarySearchTree()

    def count_top_words(self, word_count: int) -> None:
        with open(self.path, "r", encoding="ascii", errors="replace") as file:
            for line in file:
                words = findall(r"\b\w+\b", line.lower())
                for word in words:
                    if len(word) > 2 and word.isalpha():
                        self.bst.insert(word)

        print(self.bst.get_sorted_words(word_count))
