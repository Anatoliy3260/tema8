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


    def preorder(self):

        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)
        return result

    def inorder(self):

        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)
        return result

    def postorder(self):

        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, node, result):
        if node is not None:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)
        return result


# Пример использования
if __name__ == "__main__":

    tree = BinaryTree()
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for v in values:
        tree.insert(v)


    print("Прямой обход (Pre-order):", tree.preorder())
    print("Симметричный обход (In-order):", tree.inorder())
    print("Обратный обход (Post-order):", tree.postorder())
