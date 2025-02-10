class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    # Отримання висоти вузла
    def get_height(self, node):
        return node.height if node else 0

    # Поворот вправо
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    # Поворот вліво
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Отримання балансу вузла
    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    # Вставка у дерево
    def insert(self, node, key):
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        # Лівий лівий випадок
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Правий правий випадок
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Лівий правий випадок
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Правий лівий випадок
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Знаходження найменшого значення
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key


# Тестування
avltree = AVLTree()
root = None
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    root = avltree.insert(root, val)

print("Найменше значення в AVL-дереві:", avltree.find_min(root))