class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Додавання елемента в дерево
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    # Знаходження максимального значення
    def find_max(self):
        if not self.root:
            return None
        return self._find_max(self.root)
    # Пошук найбільшого значення, яке знаходиться у крайньому правому вузлі
    def _find_max(self, node):
        
        current = node
        while current.right is not None:
            current = current.right
        return current.value


# Тестування алгоритму
tree = BinarySearchTree()
values = [10, 20, 5, 15, 30, 25]
for val in values:
    tree.insert(val)

print("Найбільше значення:", tree.find_max())