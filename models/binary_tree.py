class TreeNode:
    def __init__(self, word):
        self.word = word
        self.count = 1
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if self.root is None:
            self.root = TreeNode(word)
        else:
            self._insert_recursive(self.root, word)

    def _insert_recursive(self, node, word):
        if word == node.word:
            node.count += 1
        elif word < node.word:
            if node.left is None:
                node.left = TreeNode(word)
            else:
                self._insert_recursive(node.left, word)
        else:
            if node.right is None:
                node.right = TreeNode(word)
            else:
                self._insert_recursive(node.right, word)

    def get_sorted_words(self, word_count: int):
        words = []
        self._inorder_traversal(self.root, words)

        n = len(words)
        for i in range(min(word_count, n)):
            max_index = i
            for j in range(i + 1, n):
                if words[j][1] > words[max_index][1]:
                    max_index = j
            words[i], words[max_index] = words[max_index], words[i]

        return words[:word_count]

    def _inorder_traversal(self, node, words):
        if node:
            self._inorder_traversal(node.left, words)
            words.append((node.word, node.count))
            self._inorder_traversal(node.right, words)
