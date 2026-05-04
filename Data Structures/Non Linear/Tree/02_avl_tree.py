class BinaryTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class AVLTree:
    def __init__(self, value) -> None:
        self.root = BinaryTree(value)

    def addChild(self, value):
        self.root = self.__insert_value(self.root, value)

    def __insert_value(self, current_node, value):

        # 1️⃣ Normal BST Insert
        if current_node is None:
            return BinaryTree(value)

        if value < current_node.data:
            left_child = self.__insert_value(current_node.left, value)
            current_node.left = left_child
            left_child.parent = current_node
        else:
            right_child = self.__insert_value(current_node.right, value)
            current_node.right = right_child
            right_child.parent = current_node

        # 2️⃣ Get Balance Factor
        bf = self.get_balance_factor(current_node)

        # 3️⃣ Handle 4 AVL Cases

        # Left Left
        if bf > 1 and value < current_node.left.data:
            return self.right_rotate(current_node)

        # Right Right
        if bf < -1 and value > current_node.right.data:
            return self.left_rotate(current_node)

        # Left Right
        if bf > 1 and value > current_node.left.data:
            current_node.left = self.left_rotate(current_node.left)
            current_node.left.parent = current_node
            return self.right_rotate(current_node)

        # Right Left
        if bf < -1 and value < current_node.right.data:
            current_node.right = self.right_rotate(current_node.right)
            current_node.right.parent = current_node
            return self.left_rotate(current_node)

        return current_node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update parents
        y.parent = z.parent
        z.parent = y

        if T2 is not None:
            T2.parent = z

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update parents
        y.parent = z.parent
        z.parent = y

        if T3 is not None:
            T3.parent = z

        return y

    def get_balance_factor(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        if node is None:
            return -1
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def display(self, traversal):
        print(f"{traversal.capitalize()} Order: ", end="")
        self.__print_tree(self.root, traversal)
        print()

    def __print_tree(self, current_node, traversal):
        if current_node is None:
            return

        if traversal == 'pre':
            print(current_node.data, end=" ")
            self.__print_tree(current_node.left, traversal)
            self.__print_tree(current_node.right, traversal)

        if traversal == 'in':
            self.__print_tree(current_node.left, traversal)
            print(current_node.data, end=" ")
            self.__print_tree(current_node.right, traversal)

        if traversal == 'post':
            self.__print_tree(current_node.left, traversal)
            self.__print_tree(current_node.right, traversal)
            print(current_node.data, end=" ")


avl_tree = AVLTree(24)
avl_tree.addChild(34)
avl_tree.addChild(54)

avl_tree.display('pre')