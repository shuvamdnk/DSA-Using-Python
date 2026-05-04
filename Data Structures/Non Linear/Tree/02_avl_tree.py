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
        left_depth = 0
        right_depth = 0
        self.__insert_value(self.root, value, left_depth, right_depth)

    def __insert_value(self, current_node, value, left_depth, right_depth):
        if value < current_node.data:
            # left
            if current_node.left is None:
                current_node.left = BinaryTree(value)
                current_node.left.parent = current_node
            else:
                self.__insert_value(current_node.left, value, left_depth+1, right_depth)
        else:
            # right
            if current_node.right is None:
                current_node.right = BinaryTree(value)
                current_node.right.parent = current_node
            else:
                self.__insert_value(current_node.right, value, left_depth, right_depth+1)

        bf = self.get_balance_factor(current_node)
        print(bf)
        if bf > 1:
            pass
        elif bf < -1:
            pass

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
        print() # Moves to a new line after finishing the traversal
    
    def __print_tree(self, current_node, traversal):
        if current_node is None:
            return
        if traversal == 'pre':
            # print
            print(current_node.data, end=" ")
            # left
            self.__print_tree(current_node.left, traversal)
            # right
            self.__print_tree(current_node.right, traversal)
        if traversal == 'in':
            # left
            self.__print_tree(current_node.left, traversal)
            # print
            print(current_node.data, end=" ")
            # right
            self.__print_tree(current_node.right, traversal)
        if traversal == 'post':
            # left
            self.__print_tree(current_node.left, traversal)
            # right
            self.__print_tree(current_node.right, traversal)
            # print
            print(current_node.data, end=" ")


avl_tree = AVLTree(24)

avl_tree.addChild(34)
avl_tree.addChild(54)

avl_tree.display('in')