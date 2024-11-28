# -*- coding: utf-8 -*-
"""
Created on Sat May 27 02:10:48 2023

@author: mjrbr
"""

import osmnx as ox
import random
import sys

# state_bounding_boxes is a list of tuples in the form "
#  State", lat_north, lat_south, lon_west, lon_east 
#  The tuples form a box around the state. Data pulled from 
# https://www.ala.org/rt/magirt/publicationsab/usa 
state_bounding_boxes  = [
    ("Alabama",              35.000, 30.150, -88.030,  -84.052),
    ("Alaska",               71.030, 51.015, -173.030, -130.000),
    ("Arizona",              37.000, 31.020, -114.052, -109.000),
    ("Arkansas",             36.030, 33.000, -94.037,  -89.037),
    ("California",           42.000, 32.032, -124.025, -114.007),
    ("Colorado",             41.000, 37.000, -109.007, -102.000),
    ("Connecticut",          42.003, 41.000, -73.045,  -71.045),
    ("Delaware",             39.051, 38.027, -75.048,  -75.000),
    ("District of Columbia", 39.000, 38.052, -77.007,  -76.052),
    ("Florida",              31.000, 24.030, -87.037,  -80.000),
    ("Georgia",              35.000, 30.021, -85.037,  -80.045),
    ("Hawaii",               22.014, 18.052, -160.015, -154.045),
    ("Idaho",                49.000, 42.000, -117.015, -111.000),
    ("Illinois",             42.030, 37.000, -91.030,  -87.030),
    ("Indiana",              41.045, 37.052, -88.007,  -84.045),
    ("Iowa",                 43.030, 40.022, -96.037,  -90.007),
    ("Kansas",               40.000, 37.000, -102.030, -94.035),
    ("Kentucky",             39.009, 36.037, -89.035,  -81.057),
    ("Louisiana",            33.001, 28.055, -94.003,  -88.049),
    ("Maine",                47.028, 42.058, -71.008,  -66.053),
    ("Maryland",             39.045, 37.052, -79.030,  -75.000),
    ("Massachusetts",        42.052, 41.013, -73.031,  -69.055),
    ("Michigan",             48.017, 41.042, -90.030,  -82.022),
    ("Minnesota",            49.023, 43.030, -97.015,  -89.030),
    ("Mississippi",          35.000, 30.000, -91.038,  -88.007),
    ("Missouri",             40.037, 36.000, -95.047,  -89.006),
    ("Montana",              49.000, 44.022, -116.003, -104.002),
    ("Nebraska",             43.000, 40.000, -104.003, -95.019),
    ("Nevada",               42.000, 35.000, -120.000, -114.003),
    ("New Hampshire",        45.021, 42.042, -72.034,  -70.035),
    ("New Jersey",           41.022, 38.055, -75.033,  -73.052),
    ("New Mexico",           37.000, 31.020, -109.003, -103.000),
    ("New York",             45.001, 40.030, -79.046,  -71.052),
    ("North Carolina",       36.036, 33.051, -84.020,  -75.025),
    ("North Dakota",         49.000, 45.056, -104.003, -96.033),
    ("Ohio",                 42.000, 38.024, -84.049,  -80.031),
    ("Oklahoma",             37.000, 33.037, -103.000, -94.026),
    ("Oregon",               46.016, 42.000, -124.035, -116.027),
    ("Pennsylvania",         42.016, 39.043, -80.031,  -74.041),
    ("Puerto Rico",          18.032, 17.055, -67.057,  -65.013),
    ("Rhode Island",         42.001, 41.008, -71.055,  -71.007),
    ("South Carolina",       35.013, 32.000, -83.022,  -78.031),
    ("South Dakota",         45.056, 42.029, -104.003, -96.026),
    ("Tennessee",            36.041, 34.058, -90.019,  -81.038),
    ("Texas",                36.030, 25.050, -105.039, -93.030),
    ("Utah",                 42.000, 37.000, -114.003, -109.000),
    ("Vermont",              45.000, 42.043, -73.036,  -71.028),
    ("U. S. Virgin Islands", 18.025, 17.040, -64.048,  -64.033),
    ("Virginia",             39.028, 36.032, -83.041,  -75.015),
    ("Washington",           49.000, 45.032, -124.046, -116.055),
    ("West Virginia",        40.038, 37.012, -82.039,  -77.044),
    ("Wisconsin",            47.007, 42.030, -92.054,  -86.045),
    ("Wyoming",              45.000, 41.000, -111.006, -104.000)
]

# regions is a dictionary comprehension that contains 
#  6 key (a region) value (list of states) pairs. The list of states are the
#  states which will be serviced within that region.
regions = {
    "Midwest_Region":    ["Illinois", "Indiana", "Iowa", "Kansas", "Michigan", 
                          "Minnesota", "Missouri", "Nebraska", "North Dakota", 
                          "Ohio", "South Dakota", "Wisconsin"],
    "Mountain_Region":   ["Arizona", "Colorado", "Idaho", "Montana", "Nevada", 
                          "New Mexico", "Oregon", "Utah", "Washington", 
                          "Wyoming"],
    "Northeast_Region":  ["Connecticut", "Delaware", "Maine", "Maryland", 
                          "Massachusetts", "New Hampshire", "New Jersey", 
                          "New York", "Ohio", "Pennsylvania", "Rhode Island", 
                          "Vermont", "West Virginia"],
    "Southeast_Region":  ["Alabama", "Arkansas", "Florida", "Georgia", 
                          "Kentucky", "Louisiana", "Mississippi", 
                          "North Carolina", "South Carolina", "Tennessee", 
                          "Virginia", "West Virginia"],
    "Southwest_Region":  ["Arizona", "Arkansas", "Louisiana", "New Mexico", 
                          "Oklahoma", "Texas"],
    "West_Coast_Region": ["California", "Idaho", "Nevada", "Oregon", 
                            "Washington"]
}


# Create groups of state bounding boxes based on the regions.
# region_bounding_boxes are a dictionary comprehension of 6 keys (regions) and
#  value (empty list) where he value will be populated with 
#  state_bounding_boxes values.
region_bounding_boxes = {region: [] for region in regions}
# print(region_bounding_boxes) # For testing
for state, lat_north, lat_south, lon_west, lon_east in state_bounding_boxes:
    for region, states in regions.items():
        if state in states:
            region_bounding_boxes[region].append((state, lat_north, lat_south, lon_west, lon_east))

# Print the grouped up state bounding boxes bases on regions
#=============================================================================
# for region, bounding_boxes in region_bounding_boxes.items():
#     print(f"{region}:")
#     for state_bounding_box in bounding_boxes:
#         state, lat_north, lat_south, lon_west, lon_east = state_bounding_box
#         print(f"{state}: N {lat_north}°, S {lat_south}°, W {lon_west}°, E {lon_east}°")
#     print() # Add newline

#=============================================================================

# Retrieve OSM data for each bounding box
# for name, north, south, east, west in state_bounding_boxes :

while True:
    random_key = random.choice(list(region_bounding_boxes.keys()))
    random_state, lat_north, lat_south, lon_west, lon_east = random.choice(region_bounding_boxes[random_key])
    
    
    print(random_key)
    print(random_state, lat_north, lat_south, lon_west, lon_east)
    
    # Define the subset range
    subset_range = 0.5
    
    # Calculate the subset latitude and longitude values
    subset_lat_north = random.uniform(lat_south + subset_range, lat_north)
    subset_lat_south = subset_lat_north - subset_range
    subset_lon_east  = random.uniform(lon_west, lon_east - subset_range)
    subset_lon_west  = subset_lon_east + subset_range
    
    subset_lat_north_formatted = "{:.3f}".format(subset_lat_north)
    subset_lat_south_formatted = "{:.3f}".format(subset_lat_south)
    subset_lon_east_formatted  = "{:.3f}".format(subset_lon_east)
    subset_lon_west_formatted  = "{:.3f}".format(subset_lon_west)
    
    print("Subset coordinates")
    print(random_state, subset_lat_north_formatted, subset_lat_south_formatted, 
          subset_lon_west_formatted, subset_lon_east_formatted)
    
    try:
        # Retrieve OSM data within the subset bounding box
        graph = ox.graph_from_bbox(subset_lat_north, subset_lat_south, subset_lon_east, subset_lon_west, network_type='all')
    
        # Retrieve OSM data within the current bounding box. Bounding box is to large
        # graph = ox.graph_from_bbox(lat_north, lat_south, lon_west, lon_east, network_type='all')

        # Example: Print the name and number of nodes in the graph
        print("Region:", random_key)
        print("Number of nodes:", len(graph.nodes))
        print(graph)

        # Extract real addresses from the OSM data
        addresses = []
        
        # For testing
        # for node_id in graph.nodes():
        #     print(node_id)
        
        checked_nodes = 0  # Counter for the number of nodes checked
        
        while True:
            random_node_id = random.choice(list(graph.nodes))
            
            node_data = graph.nodes[random_node_id]
            # print("Node ID:", random_node_id)
            # print("Attributes:", list(node_data.keys()))
            
            checked_nodes += 1

            # Update the terminal output with the new counter
            sys.stdout.write("\rNodes checked: {}".format(checked_nodes))
            sys.stdout.flush()
            
            if 'addr:street' in node_data and 'addr:housenumber' in node_data:
                street = node_data['addr:street']
                housenumber = node_data['addr:housenumber']
                address = f"{housenumber} {street}"
                print("Address:", address)
                break


        # The following works to get one or fail above will keep looking until
        #  it finds address information
        # random_node_id = random.choice(list(graph.nodes))
        
        # if random_node_id in graph.nodes:
        #     node_data = graph.nodes[random_node_id]
        #     print("Node ID:", random_node_id)
        #     print("Attributes:", list(node_data.keys()))
        # else:
        #     print("Node ID", random_node_id, "does not exist in the graph.")
            
        # if 'addr:street' in node_data and 'addr:housenumber' in node_data:
        #     street = node_data['addr:street']
        #     housenumber = node_data['addr:housenumber']
        #     address = f"{housenumber} {street}"
        #     print("Address:", address)
        # else:
        #     print("Address information not available for this node.")

        
        # for node in graph.nodes:
        #     print("Inside graph.nodes for loop before if")
        #     if 'addr:street' in graph.nodes[node] and 'addr:housenumber' in graph.nodes[node]:
        #          street = graph.nodes[node]['addr:street']
        #          housenumber = graph.nodes[node]['addr:housenumber']
        #          address = f"{housenumber} {street}"
        #          print("Inside for if loop")
        #          addresses.append(address)

        # Print the list of addresses
        for address in addresses:
            print("inside for loop addresses")
            print(address)


        break # Break the loop if data retrieval is successful
    except ValueError as e:
        print("No data elements found in the response JSON. Trying another random Region")
        continue # Retry with another random selection
    
