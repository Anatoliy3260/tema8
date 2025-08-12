from collections import deque


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node


        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))


        return self._balance(node)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _balance(self, node):
        balance = self._get_balance(node)


        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)


        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)


        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)


        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def bfs(self):

        if not self.root:
            return []

        result = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result.append(node.key)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def inorder(self):

        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        return result


# Пример использования
if __name__ == "__main__":
    avl = AVLTree()

    print("Вставка элементов в AVL-дерево:")
    elements = [10, 20, 30, 40, 50, 25]
    for el in elements:
        print(f"Вставляем {el}")
        avl.insert(el)
        print(f"BFS после вставки {el}: {avl.bfs()}")
        print(f"Высота дерева: {avl._get_height(avl.root)}")
        print("-" * 40)

    print("\nИтоговое дерево:")
    print("BFS обход:", avl.bfs())
    print("Inorder обход (отсортировано):", avl.inorder())
    print(f"Высота дерева: {avl._get_height(avl.root)}")