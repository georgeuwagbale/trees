import Graph as GP

road_networks = ["Lagos", "Ogun", "Ekiti", "Osun", "Ondo", "Edo", "Kwara"]

nodes = {}
for road_network in road_networks:
    nodes.update({road_network: GP.create_node(road_network)})

# Undirected connection between Lagos and Ogun
GP.add_to_graph(nodes.get("Lagos"), nodes.get("Ogun"), 89.7)
GP.add_to_graph(nodes.get("Ogun"), nodes.get("Lagos"), 89.7)

# Undirected connection between Lagos and Ekiti
GP.add_to_graph(nodes.get("Lagos"), nodes.get("Ekiti"), 337.2)
GP.add_to_graph(nodes.get("Ekiti"), nodes.get("Lagos"), 337.2)

# Undirected connection between Lagos and Kwara
GP.add_to_graph(nodes.get("Lagos"), nodes.get("Kwara"), 355.7)
GP.add_to_graph(nodes.get("Kwara"), nodes.get("Lagos"), 355.7)

# Undirected connection between Ogun and Ekiti
GP.add_to_graph(nodes.get("Ogun"), nodes.get("Ekiti"), 309.3)
GP.add_to_graph(nodes.get("Ekiti"), nodes.get("Ogun"), 309.3)

# Undirected connection between Ekiti to Osun
GP.add_to_graph(nodes.get("Ekiti"), nodes.get("Osun"), 132)
GP.add_to_graph(nodes.get("Osun"), nodes.get("Ekiti"), 132)

# Undirected connection between Osun to Edo
GP.add_to_graph(nodes.get("Osun"), nodes.get("Edo"), 253.8)
GP.add_to_graph(nodes.get("Edo"), nodes.get("Osun"), 253.8)

# Undirected connection between Edo to Ondo
GP.add_to_graph(nodes.get("Edo"), nodes.get("Ondo"), 197.5)
GP.add_to_graph(nodes.get("Ondo"), nodes.get("Edo"), 197.5)

# Undirected connection between Ekiti to Ondo to and fro
GP.add_to_graph(nodes.get("Ekiti"), nodes.get("Ondo"), 120.4)
GP.add_to_graph(nodes.get("Ondo"), nodes.get("Ekiti"), 120.4)

# Undirected connection between Kwara and Edo
GP.add_to_graph(nodes.get("Kwara"), nodes.get("Edo"), 451.2)
GP.add_to_graph(nodes.get("Edo"), nodes.get("Kwara"), 451.2)


def optimal(first_location, second_location, visited=[]):

    if first_location is second_location or second_location in first_location.connections:
        return "Arrived"

    visited.append(first_location)
    for connection in first_location.connections:
        if connection not in visited:
            optimal(connection, second_location)




print(optimal(nodes.get("Lagos"), nodes.get("Ondo")))