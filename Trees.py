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

    if n_value > root_node.get_data():
        search_tree(root_node.right, n_value)

    if n_value < root_node.get_data():
        search_tree(root_node.left, n_value)

    if root_node.get_data() == n_value:
        root_node.set_data(n_value)

    return root_node.get_data()



def delete_leaf_nodes(root_node):
    if root_node.right is None and root_node.left is None:
        return None

    if root_node.left:
        root_node.left = delete_leaf_nodes(root_node.left)

    if root_node.right:
        root_node.right = delete_leaf_nodes(root_node.right)

    return root_node


def display_leaf_nodes(root_node):
    if root_node is None:
        return []

    return display_leaf_nodes(root_node.left) + display_leaf_nodes(root_node.right) + [
        root_node.get_data() for _ in range(1) if root_node.left is None and root_node.right is None]


def display_inorder(root_node):
    if root_node is None:
        return []

    return display_inorder(root_node.left) + [root_node.get_data()] + display_inorder(root_node.right)


def get_odd_values(root_node):
    if root_node is None:
        return []

    return get_odd_values(root_node.left) + get_odd_values(root_node.right) + [
        root_node.get_data() for _ in range(1) if root_node.get_data() % 2 == 1]


def delete_leaf_target(root_node, target):
    if root_node is None:
        return None

    if root_node.left:
        root_node.left = delete_leaf_target(root_node.left, target)

    if root_node.right:
        root_node.right = delete_leaf_target(root_node.right, target)

    if root_node.right is None and root_node.left is None and root_node.get_data() == target:
        return None

    return root_node


def get_subtree(root_node, target_value):
    if root_node is None:
        return None

    if root_node.get_data() == target_value:
        return display_inorder(root_node)

    if root_node.left:
        get_subtree(root_node.left, target_value)

    if root_node.right:
        get_subtree(root_node.right, target_value)


values = [5, 4, 1, 3, 7, 0, 3]
head_node = Node(values[0])

for value in values:
    if value is not values[0]:
        new_node = Node(value)
        create_tree(head_node, new_node)

# print(get_odd_values(head_node))

#print(get_subtree(head_node, 7))
print(search_tree(head_node, 4))
