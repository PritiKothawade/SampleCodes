class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data)

    def traverse_in_order(self, node):
        if node is None:
            return

        self.traverse_in_order(node.left)
        print(node.data, "->", end='')
        self.traverse_in_order(node.right)


class TreeComparator(object):

    def compare(self, node1, node2):

        if not node1 or not node2:
            return node1 == node2

        if node1.data != node2.data:
            return False

        return self.compare(node1.left, node2.left) and self.compare(node1.right, node2.right)


if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.insert(10)
    bst1.insert(20)
    bst1.insert(5)
    bst1.insert(15)
    bst1.traverse_in_order(bst1.root)

    print("""""""")

    bst2 = BinarySearchTree()
    bst2.insert(10)
    bst2.insert(20)
    bst2.insert(5)
    bst2.insert(15)
    bst2.traverse_in_order(bst2.root)

    print("""""""")

    tc = TreeComparator()
    print(tc.compare(bst1.root, bst2.root))


