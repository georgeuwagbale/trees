# Created by georgeuwagbale on 25/06/2022

class Node:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.edges_weight = {}

    def __str__(self):
        return f"Node_name: {self.name}; Connected_nodes: {[_edge.name for _edge in self.connections]}"


def create_node(name):
    new_node = Node(name)
    return new_node


def add_to_graph(node, new_node, edge_weight):
    node.connections.append(new_node)
    add_edge_weight(node, new_node, edge_weight)
    return f"{node.name} connected to {new_node.name}"


def add_edge_weight(node, new_node, value):
    if new_node in node.connections:
        if value:
            node.edges_weight.update({new_node.name: value})
        else:
            edge_weight = int(input(f"Enter edge weight between {node.name} and {new_node.name}: "))
            node.edges_weight.update({new_node.name: edge_weight})
    else:
        print(f"There is not edge connecting {node.name} and {new_node.name}")


"""
networks = ["Lagos", "Abuja", "Kwara", "Benin", "Asaba"]
graph = Node(networks[0])
for network in networks:
    if network != networks[0]:
        add_to_graph(graph, create_node(network))

print(graph)

"""