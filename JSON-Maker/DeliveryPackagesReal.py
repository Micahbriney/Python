# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:20:33 2023

@author: Micah Briney

Usage: 
    1. Enter in the number of deliberies that you want to create.
    2. Enter in the maximum number of packages that will be randomly created for
       each delivery
    3. Enter in the state or US territory you want the delivery('s) pickup and 
       destination. Input "all" to randomly choose a pickup and desitination 
       state/territory. Typos will default to all
    4. Wait till program finishes
"""

from datetime import datetime, timedelta
from faker import Faker
from geopy.geocoders import Nominatim
import json
import math
import phonenumbers
import random
import sys
import requests


# Set the request headers
headers = {
    "Content-Type": "text/plain",
    "User-Agent": "PostmanRuntime/7.32.2",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}



"""
Generate a dictionary comprehension of regions that have latitude and longitude 
 bounding boxes associated with States. These states are associated with 
 shipping regions. Ajust the region states as necessary.

Args:
    None.
Returns:
    dict: Region dictionary comprehension.
"""
def generateRegionBoundingBoxes():    
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
                
    return region_bounding_boxes


"""
Generate a random address by reverse geocoding random latitude and longitude within a specific range.

Args:
    geocoder: Geocoder object.
    bounding_box: Latitude, Longitude box about a givin state.
Returns:
    dict: Address components dictionary.
"""
def generateRealRandomAddress(geocoder, region_bounding_boxes, input_state):

    address_components = {
        'Address': None,
        'House Address': None,
        'Street': None,
        'City': None,
        'State': None,
        'Postal Code': None,
        'Latitude' : None,
        'Longitude' : None,
        'State Abbreviation': None,
        'Country Abbreviation': None
    }


    if input_state == "All":
        # print("Using Random State Lat and Long") # For testing
        region = random.choice(list(region_bounding_boxes.keys()))
        state, lat_north, lat_south, lon_west, lon_east = random.choice(region_bounding_boxes[region])
    else: # Find region info for user input state
        for region in region_bounding_boxes:
            # print(f"Looking for {input_state} in", region) # For testing
            # print("Region info: ", region_bounding_boxes["Midwest_Region"])
            for state_info in region_bounding_boxes[region]:
                state_name = state_info[0]
                # print(f"Does state name {state_name} match?") # For testing
                if state_name == input_state:
                    # state, lat_north, lat_south, lon_west, lon_east = region_bounding_boxes[region]
                    state, lat_north, lat_south, lon_west, lon_east = state_info
                    # print("Found the State") # For Testing
                    # print(state)
                    # print(lat_north)
                    # print(lat_south)
                    # print(lon_west)
                    # print(lon_east)
                    break;


    
    missed_locations = 1

    while any(value is None for value in address_components.values()):
        # Reset address components to None
        for key in address_components:
            address_components[key] = None


        # Generate random latitude and longitude within specified state
        latitude = random.uniform(lat_north, lat_south)
        longitude = random.uniform(lon_west, lon_east)        

        # Reverse geocode the coordinates to obtain the address
        location = geocoder.reverse((latitude, longitude))

        if location is not None:
            address = location.address

            # Extract specific parts of the address
            address_components['Address'] = address
            address_components['House Address'] = location.raw['address'].get('house_number')
            address_components['Street'] = location.raw['address'].get('road')
            address_components['City'] = location.raw['address'].get('city') or \
                                         location.raw['address'].get('town') or \
                                         location.raw['address'].get('village') or \
                                         location.raw['address'].get('hamlet') or \
                                         location.raw['address'].get('suburb')
            address_components['State'] = location.raw['address'].get('state')
            address_components['Postal Code'] = location.raw['address'].get('postcode')
            address_components['Latitude'] = location.raw.get('lat')
            address_components['Longitude'] = location.raw.get('lon')
            iso_code = location.raw['address'].get('ISO3166-2-lvl4')
            if iso_code:
                state_abbr, country_abbr = iso_code.split('-')
                address_components['State Abbreviation'] = state_abbr
                address_components['Country Abbreviation'] = country_abbr
            # print("Test Locations checked:", missed_locations)
        # else:
        # Update the terminal output with the new counter
        sys.stdout.write("\rLocations checked: {}".format(missed_locations))
        sys.stdout.flush() # For testing
        missed_locations += 1
    print() #For Testing
    
    return address_components



"""
Prompt and parse the user input

Args:
    none
Returns:
    user_state_input:   State name
    user_count_input:   Number of deliveries
    user_package_input: Max number of packages
"""
def getUserInput():
    valid_inputs = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts",
        "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
        "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island",
        "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
        "U. S. Virgin Islands", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]

    user_count_input   = -1 # Initialize user_number with an invalid value
    user_package_input = -1 # Initialize user_number with an invalid value
    
    while user_count_input < 0:
        user_count_input = input("How many deliveries do you want to create: ")
        try:
            user_count_input = int(user_count_input)
            if user_count_input < 0:
                print(f"Invalid number '{user_count_input}'. Please enter a non-negative number.")
                user_count_input = -1  # Reset user_count_input for re-prompt
            else:
                break
        except ValueError:
            print("Invalid input '{user_count_input}'. Please enter a valid non-negative number.")
            user_count_input = -1  # Reset user_count_input for re-prompt

    while user_package_input < 0:
        user_package_input = input("Enter max number of packages for each delivery: ")
        try:
            user_package_input = int(user_package_input)
            if user_package_input < 0:
                print(f"Invalid number '{user_package_input}'. Please enter a non-negative number.")
                user_package_input = -1  # Reset user_package_input for re-prompt
            else:
                break
        except ValueError:
            print("Invalid input '{user_package_input}'. Please enter a valid non-negative number.")
            user_package_input = -1  # Reset user_package_input for re-prompt


    user_state_input = input("Please enter the name of a state or US territory (or 'all' for all): ")
    user_state_input = user_state_input.lower().title()  # Capitalize each word in the user's input

    if user_state_input in valid_inputs:
        # User entered a valid state or territory
        # Perform your logic for the specific state/territory here
        print(f"Creating {user_count_input} delivery(ies) in or around {user_state_input}...")
    elif user_state_input == "All":
        # User entered 'all'
        # Perform your logic for 'all' here
        print(f"Creating {user_count_input} delivery(ies) in a random US state or territory...")
    else:
        # User entered an invalid input
        # Default to 'all' here
        print(f"Invalid input '{user_state_input}'. Using default \"All\".")
        print(f"Creating {user_count_input} delivery(ies) in a random US state or territory...")

    return user_state_input, user_count_input, user_package_input


"""
Caclulate the spherical distance between two points

Args:
    lat1: Pickup latitude
    lon1: Pickup longitude
    lat2: Destination latitude
    lon2: Destination longitude
Returns:
    distance: Spherical distance between two points
"""
def calculateDistance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Earth's radius in miles
    radius = 3958.8

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    
    return round(distance, 2)


"""
Create an active delivery JSON and populate it with data

Args:
    geocoder: Address information
    state:    State name
    count:    
    region_bounding_boxes: dictionary comprehension of regions/state data
Returns:
    data: Active Delivery JSON
"""
# def buildActiveDeliveryJSON(geocoder, state, count, region_bounding_boxes):
def buildActiveDeliveryJSON(geocoder, state, region_bounding_boxes):
    
    fake = Faker()
    
    
    # Generate pickup and destination times
    pickup_time_from = datetime.now() + timedelta(days=1)
    pickup_time_to = pickup_time_from + timedelta(hours=2)
    dest_time_from = datetime.now() + timedelta(days=2)
    dest_time_to = dest_time_from + timedelta(hours=4)
    
    # Ensure pickupTimeFrom is less than pickupTimeTo
    if pickup_time_from > pickup_time_to:
        pickup_time_from, pickup_time_to = pickup_time_to, pickup_time_from
    
    # Ensure destTimeFrom is less than destTimeTo
    if dest_time_from > dest_time_to:
        dest_time_from, dest_time_to = dest_time_to, dest_time_from
    
    # Generate random dollar value
    offer_amt = round(random.uniform(0, 10000), 2)
    
    # Generate radom package amount numOfPackages
    num_pkgs = round(random.uniform(0, 0))
    
    # Generate real county, state, city, street data
    print()
    print("Getting Pickup info")
    pickup_address_components = generateRealRandomAddress(geocoder, region_bounding_boxes, state)
    print("Getting Delivery info")
    dest_address_components = generateRealRandomAddress(geocoder, region_bounding_boxes, state)
    
    distance_in_miles = calculateDistance(float(pickup_address_components['Latitude']),
                                         float(pickup_address_components['Longitude']),
                                         float(dest_address_components['Latitude']),
                                         float(dest_address_components['Longitude']))
    
    
    pickup_country_code = "US"
    dest_country_code = "US"
    # International
    # pickup_country_code = random.choice(list(pycountry.countries)).alpha_2
    # pickup_state = fake.state_abbr()
    # dest_country_code = random.choice(list(pycountry.countries)).alpha_2
    # dest_state = fake.state_abbr()
    
    # Generate random phone numbers
    pickup_phone_number = phonenumbers.format_number(phonenumbers.parse(
        fake.phone_number(), pickup_country_code),
        phonenumbers.PhoneNumberFormat.E164)
    dest_phone_number = phonenumbers.format_number(phonenumbers.parse(
        fake.phone_number(), dest_country_code),
        phonenumbers.PhoneNumberFormat.E164)
    
    
    # Construct JSON object
    data = {
        "shippersPO": "hello",
        "paymentTerms": "payment",
        "paymentType": "type",
        "offerAmt": str(offer_amt),
        "numOfPackages": str(num_pkgs),
        "deliveryDistMiles": str(distance_in_miles),
        "deliveryTimeMin": "0",
        "pickup": {
            "pickupTimeTo": pickup_time_to.strftime('%Y-%m-%dT%H:%M:%S'),
            "pickupTimeFrom": pickup_time_from.strftime('%Y-%m-%dT%H:%M:%S'),
            "pickupName": fake.name(),
            "pickupPhoneNum": pickup_phone_number,        
            "pickupAddress": pickup_address_components['House Address'] + ', ' + pickup_address_components['Street'],
            "pickupCity": pickup_address_components['City'],
            "pickupState": pickup_address_components['State'],
            "pickupCountry": pickup_address_components['Country Abbreviation'],
            "pickupZip": pickup_address_components['Postal Code'],        
            "pickupEmail": fake.email(),
            "rescueInst": "rescue",        
            "pickupLatitude" : pickup_address_components['Latitude'],
            "pickupLongitude" : pickup_address_components['Longitude']
        },
        "destination": {
            "destTimeTo": dest_time_to.strftime('%Y-%m-%dT%H:%M:%S'),
            "destTimeFrom": dest_time_from.strftime('%Y-%m-%dT%H:%M:%S'),
            "destPhoneNum": dest_phone_number,
            "destAddress": dest_address_components['House Address'] + ', ' + dest_address_components['Street'],
            "destCountry": dest_address_components['Country Abbreviation'],
            "destCity": dest_address_components['City'],
            "destState": dest_address_components['State'],
            "destZip": dest_address_components['Postal Code'],
            "destEmail": fake.email(),
            "destName" : "Not Here",
            "destLatitude" : dest_address_components['Latitude'],
            "destLongitude" : dest_address_components['Longitude']
        },
        "chat" : "...Python generator...",
        "status" : "Available"
    }
    
    return data

"""
Create an active delivery JSON and populate it with data

Args:
    uid: UID of the recently created active delivery    
Returns:
    data: Package JSON
"""
def buildAddPackageJSON(uid):

    # Generate random values
    package_depth = round(random.uniform(1.0, 2.0), 2)
    package_unit = round(random.uniform(1.0, 2.0), 2)
    package_width = round(random.uniform(1.0, 2.0), 2)
    package_weight_major = round(random.uniform(10.0, 40000.0), 2)

    data = {
        "deliveryUid" : uid,
        "packageSize" : {
            "packageDepth" : str(package_depth),
            "packageUnit" : str(package_unit),
            "packageWidth" : str(package_width)
            },
        "packageWeight" : {
            "weightMajor" : str(package_weight_major),
            "weightMinor" : "0",
            "weightUnitSystem" : "kg"
            }
        }

    return data



# Initialize the geocoder with a user agent
geocoder = Nominatim(user_agent='my-app')

# Get user input for number of deliveries and Location
state, count, num_packages = getUserInput()


# Create bounding box for shipping regions
region_bounding_boxes = generateRegionBoundingBoxes()

# loop for the number of deliveries specified by the user input count variable
for i in range(count):
    
    # data = buildActiveDeliveryJSON(geocoder, state, count, region_bounding_boxes)
    data = buildActiveDeliveryJSON(geocoder, state, region_bounding_boxes)

    
    print(f"\nDelivery: {i + 1}\n")
    print(json.dumps(data, indent=4))
    
    json_payload = json.dumps(data)
    # Print a copy and pasteable json
    # print(json_payload) # For testing
    
    # Send the POST request
    response = requests.post("https://api.macchinoodle.com/prod/addActiveDelivery", data=json_payload, headers=headers)
    
    # Check the response status code
    if response.status_code == 200:
        print("\nPOST request successful.")
    else:
        print("\nPOST request failed.")
    
    # Extract information from the response
    status_code = response.status_code
    headers = response.headers
    content = response.content
    json_data = response.json()
    uid = json_data['uid']
    
    # Print the response message. For testing
    # print("Status Code:", status_code)
    # print("Headers:", headers)
    # print("Content:", content)
    # print("JSON Data:", json_data)
    # print("UID:", uid)
    
    # Pick a random amount of packages to create for the current delivery
    # rand_num_packages = range(random.randint(1, num_packages))
    
    rand_num_packages = random.randint(1, num_packages)
    
    print(f"\nCreating {rand_num_packages} random packages for delivery {i + 1}\n")
    
    # Loop for each package to be created
    for j in range(rand_num_packages):
        
        add_package = buildAddPackageJSON(uid)
        
        print(json.dumps(add_package, indent=4))
        
        json_payload = json.dumps(add_package)
        
        # Send the POST request
        response = requests.post("https://api.macchinoodle.com/prod/addPackage", data=json_payload, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            print("POST request successful.")
        else:
            print("POST request failed.")

# Output JSON object
# print(json.dumps(data, indent=4))
