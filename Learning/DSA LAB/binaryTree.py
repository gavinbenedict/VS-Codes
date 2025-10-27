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

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def display_tree(self, node=None, space=0, level_spacing=5):
        if node is None:
            node = self.root
        if node is None:
            print("Tree is empty")
            return
        space += level_spacing
        if node.right:
            self.display_tree(node.right, space)
        print(" " * (space - level_spacing) + str(node.value))
        if node.left:
            self.display_tree(node.left, space)

tree = BinaryTree()
print("Enter values to insert into the binary tree (type 'done' to stop):")
while True:
    user_input = input("Enter value: ")
    if user_input.lower() == 'done':
        break
    try:
        value = int(user_input)
        tree.insert(value)
    except ValueError:
        print("Please enter a valid integer.")
print("\nConstructed Binary Tree:")
tree.display_tree()
