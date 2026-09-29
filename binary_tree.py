class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


# Create the binary tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)


# Display traversals
print("Inorder:", inorder(root))
print("Preorder:", preorder(root))
print("Postorder:", postorder(root))