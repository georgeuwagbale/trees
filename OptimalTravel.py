from Middleware import road_networks

print("Available locations")
for road_network in road_networks:
    print("- ", road_network)

first_location = input("Enter first location: ")
second_location = input('Enter second: ')

