from typing import Any

class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data) -> None:
        self.root = BinaryTreeNode(data)

    def addChild(self, value):
        self.__insert_recursive(self.root, value)

    def __insert_recursive(self, current_node, value):
        if value < current_node.data:
            # left side
            if current_node.left is None:
                current_node.left = BinaryTreeNode(value)
            else:
                self.__insert_recursive(current_node.left, value)
        elif value > current_node.data:
             # right side
            if current_node.right is None:
                current_node.right = BinaryTreeNode(value)
            else:
                self.__insert_recursive(current_node.right, value)
    
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

    def search(self, value):
        self.__search_node(self.root, value)

    def __search_node(self, current_node, value):
        if  value == current_node.data:
            print('Found')
            return
        if value < current_node.data:
            if current_node.left is not None:
                self.__search_node(current_node.left, value)
            else:
                print("Not Found")
                return
            
        if value > current_node.data:
            if current_node.right is not None:
                self.__search_node(current_node.right, value)
            else:
                print("Not Found")
                return

    def search_detailed(self, value):
        # We pass 0 as the starting depth and an empty list for the path
        return self.__search_detailed_node(self.root, value, 0, [])

    def __search_detailed_node(self, current_node, value, depth, path):
        # 1. Base Case: Not Found
        if current_node is None:
            return {"status": "Not Found", "visited": path}

        # Add current node to the path of visited nodes
        path.append(current_node.data)

        # 2. Base Case: Found!
        if value == current_node.data:
            return {
                "status": "Found",
                "memory_id": id(current_node),
                "depth": depth,
                "path": path,
                "distance_from_root": depth  # Depth is essentially distance
            }

        # 3. Recursive Steps
        if value < current_node.data:
            return self.__search_detailed_node(current_node.left, value, depth + 1, path)
        else:
            return self.__search_detailed_node(current_node.right, value, depth + 1, path)

            
           
root = BinarySearchTree(25)

root.addChild(20)
root.addChild(120)
root.addChild(105)

# root.display('in')
# root.display('pre')
# root.display('post')

print(root.search_detailed(105))