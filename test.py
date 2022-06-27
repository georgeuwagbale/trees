#Created by georgeuwagbale on 26/06/2022

class Edge:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None
        self.nodes = None
        self.weight = 0

    def __str__(self):
        return f"{self.name}"


class Node:
    def __init__(self, name):
        self.name = name
        self.edges = None

    def __str__(self):
        return f"{self.name}"


def create_node(name):
    created_node = Node(name)
    return created_node


def create_edge(name):
    created_edge = Edge(name)
    return created_edge


node_name_list = ["Lagos", "Ogun", "Ekiti", "Osun", "Ondo", "Edo", "Kwara"]
node_name = {}

edges = {}

for node in node_name_list:
    new_node = create_node(node)
    node_name.update({new_node.name: new_node})


# lagos = Node("Lagos")
# ogun = Node("Ogun")
# ekiti = Node("Ekiti")

"""
edge_amount = 9
for i in range(edge_amount):
    edge_name = input("Enter edge name: ")
    new_edge = create_edge(edge_name)
    edges.update({edge_name: new_edge})
"""

lagos__ogun = Edge("lagos__ogun")
lagos__ogun.weight = 89.7
ogun__ekiti = Edge("ogun__ekiti")
ogun__ekiti.weight = 309.3
ekiti__ondo = Edge("ekiti_ondo")
ekiti__ondo.weight = 120.4

lagos__ekiti = Edge("lagos__ekiti")
lagos__ekiti.weight = 337.2


lagos__ogun.next = ogun__ekiti
ogun__ekiti.prev = lagos__ogun

ogun__ekiti.next = lagos__ekiti
lagos__ekiti.prev = ogun__ekiti

lagos__ekiti.prev = lagos__ogun


lagos__ogun.nodes = [node_name.get("Lagos"), node_name.get("Ogun")]
ogun__ekiti.nodes = [node_name.get("Ogun"), node_name.get("Ekiti")]
lagos__ekiti.nodes = [node_name.get("Ekiti"), node_name.get("Lagos")]

# lagos.edges = [edge_1, edge_3]
node_name.get("Lagos").edges = [lagos__ekiti, lagos__ogun]
node_name.get("Ogun").edges = [lagos__ogun, ogun__ekiti]
node_name.get("Ekiti").edges = [lagos__ekiti]

def adder(values):
    result = 0
    for value in values:
        result += value
    return result


def fun(edge, dest_node, weights):
    weights.update({f"{edge.name}": edge.weight})
    if dest_node in edge.nodes:
        return weights

    fun(edge.next, dest_node, weights)
    return weights


def process(data):
    value = 0
    info_keys = data.keys()
    for key in info_keys:
        value += data.get(key)
    return {f"{list(info_keys)}": f"{value}KM"}


def optimal(node, dest_node, result={}):
    if node is dest_node:
        return f"You in {node.name} already."
    for edge in node.edges:
        data = process(fun(edge, dest_node, weights={}))
        result.update(data)
    return result


print(optimal(node_name.get('Lagos'), node_name.get("Ekiti")))
