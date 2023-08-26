class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
           self.insert_helper(self.root, new_node)

    def insert_helper(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self.insert_helper(current_node.left, new_node)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self.insert_helper(current_node.right, new_node)

    def search(self, value):
        return self.search_helper(self.root, value)

    def search_helper(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        elif current_node.value < value:
            return self.search_helper(current_node.right, value)
        else:
            return self.search_helper(current_node.left, value)


def main():
    # Instantiate BST
    bst = BST()

    # Insert into BST
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)

    # Search BST
    print(bst.search(3)) # Prints true
    print(bst.search(10)) # Prints false


if __name__ == "__main__":
        main()


