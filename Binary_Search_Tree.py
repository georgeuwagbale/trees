# Create Binary Search Tree
def create_bst(root_node, node):
    if root_node is None:
        return None

    if node.get_data() < root_node.get_data():
        if root_node.left:
            create_bst(root_node.left, node)
        else:
            root_node.left = node

    if node.get_data() > root_node.get_data():
        if root_node.right:
            create_bst(root_node.right, node)
        else:
            root_node.right = node
