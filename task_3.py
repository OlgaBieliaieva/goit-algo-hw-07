class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка елементів у дерево
    def insert(self, value):
        if self.root is None:
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

    # Обчислення суми всіх значень у дереві
    def sum_values(self):
        return self._sum_values(self.root)

    def _sum_values(self, node):
        if node is None:
            return 0
        # Сума значення вузла + рекурсивні виклики для піддерев
        return node.value + self._sum_values(node.left) + self._sum_values(node.right)


# Тестування
tree = BinarySearchTree()
values = [10, 5, 15, 3, 7, 12, 18]
for val in values:
    tree.insert(val)

print("Сума всіх значень у дереві:", tree.sum_values())