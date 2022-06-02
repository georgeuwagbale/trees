class Node:
    def __init__(self, data):
        self.__data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


def create_tree(root_node, node):
    if root_node is None:
        return None

    if node.get_data() < root_node.get_data():
        if root_node.left:
            create_tree(root_node.left, node)
        else:
            root_node.left = node

    if node.get_data() > root_node.get_data():
        if root_node.right:
            create_tree(root_node.right, node)
        else:
            root_node.right = node


def search_tree(root_node, n_value):
    if root_node is None:
        return None

    if root_node.get_data() == n_value:
        return "Found value"

    if n_value > root_node.get_data():
        search_tree(root_node.right, n_value)

    if n_value < root_node.get_data():
        search_tree(root_node.left, n_value)


def delete_leaf_nodes(root_node):
    if root_node.right is None and root_node.left is None:
        return None

    if root_node.left:
        root_node.left = delete_leaf_nodes(root_node.left)

    if root_node.right:
        root_node.right = delete_leaf_nodes(root_node.right)

    return root_node


def display_inorder(root_node):
    if root_node is None:
        return []

    return display_inorder(root_node.left) + [root_node.get_data()] + display_inorder(root_node.right)


def get_odd_values(root_node):
    if root_node is None:
        return []

    return get_odd_values(root_node.left) + get_odd_values(root_node.right) + [
        root_node.get_data() for _ in range(1) if root_node.get_data() % 2 == 1]


values = [5, 4, 1, 6, 7, 0, 3]
head_node = Node(values[0])

for value in values:
    if value is not values[0]:
        new_node = Node(value)
        create_tree(head_node, new_node)

print(get_odd_values(head_node))

