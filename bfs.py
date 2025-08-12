from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def bfs(self):

        if self.root is None:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)


            if current_node.left:
                queue.append(current_node.left)


            if current_node.right:
                queue.append(current_node.right)

        return result


# Пример использования
if __name__ == "__main__":
    # Создаем бинарное дерево
    tree = BinaryTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    print("Вставляем значения в дерево:", values)
    for v in values:
        tree.insert(v)

    # Выполняем обход в ширину
    bfs_result = tree.bfs()
    print("\nРезультат BFS обхода:", bfs_result)

    print("Порядок обхода BFS соответствует уровням дерева сверху вниз, слева направо")