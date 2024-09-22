class BinaryNode:
    def __init__(self, value):
        self.left = None
        self.data = value  # Use data instead of value for consistency
        self.right = None


class BinaryTreeOrder:
    def create_node(self, data):  # Use snake_case for function names
        return BinaryNode(data)

    def insert(self, node, data):
        if node is None:
            return self.create_node(data)  # Return the newly created node

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node  # Return the modified node (not strictly necessary here)

    def print_inorder(self, root): #Left, root, right
        if root is not None:
            self.print_inorder(root.left)
            print(root.data)
            self.print_inorder(root.right)  # Fix the duplicate call to root.left
    
    def print_preorder(self, root): # root, lift,  right
        if root is not None:
            print(root.data)
            self.print_preorder(root.left)
            self.print_preorder(root.right) 
    
    def print_postorder(self, root): #Left, right, root
        if root is not None:
            self.print_postorder(root.left)
            self.print_postorder(root.right) 
            print(root.data)

    def print_reverse(self, root): #right, root, Left
         if root is not None:
            self.print_reverse(root.right)
            print(root.data)
            self.print_reverse(root.left) 

tree = BinaryTreeOrder()
root = tree.create_node(5)
print(root.data)
tree.insert(root, 2)
tree.insert(root, 10)
tree.insert(root, 7)
tree.insert(root, 15)
tree.insert(root, 12)
tree.insert(root, 20)
tree.insert(root, 30)
tree.insert(root, 6)
tree.insert(root, 8)
print('In Order =====> \n')
tree.print_inorder(root)

print('Pre Order =====> \n')
tree.print_preorder(root)

print('Post Order =====> \n')
tree.print_postorder(root)

print('Reverse =====> \n')
tree.print_reverse(root)