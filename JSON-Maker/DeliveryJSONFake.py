"""
@author: Micah Briney

Creates an active delivery JSON with fake random data. Used 
for manual copy and pasting

Usage: 
    1. Run program and wait for output.
"""

import json
import random
import uuid
from datetime import datetime, timedelta
import phonenumbers
import pycountry
from faker import Faker

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
offer_amt = round(random.uniform(0, 10000000), 2)

# Generate radom package amount numOfPackages
num_pkgs = round(random.uniform(0, 1000))


# Generate random countries and states/provinces
pickup_country_code = random.choice(list(pycountry.countries)).alpha_2
pickup_state = fake.state_abbr()
dest_country_code = random.choice(list(pycountry.countries)).alpha_2
dest_state = fake.state_abbr()

# Generate random phone numbers
pickup_phone_number = phonenumbers.format_number(phonenumbers.parse(
    fake.phone_number(), pycountry.countries.get(alpha_2=pickup_country_code).alpha_2),
    phonenumbers.PhoneNumberFormat.E164)
dest_phone_number = phonenumbers.format_number(phonenumbers.parse(
    fake.phone_number(), pycountry.countries.get(alpha_2=dest_country_code).alpha_2),
    phonenumbers.PhoneNumberFormat.E164)


# Construct JSON object
data = {
    "shippersPO": "hello",
    "paymentTerms": "payment",
    "paymentType": "type",
    "offerAmt": str(offer_amt),
    "numOfPackages": 0,
    "pickup": {
        "pickupTimeTo": pickup_time_to.strftime('%Y-%m-%dT%H:%M:%S'),
        "pickupTimeFrom": pickup_time_from.strftime('%Y-%m-%dT%H:%M:%S'),
        "pickupName": fake.name(),
        "pickupPhoneNum": pickup_phone_number,
        "pickupAddress": fake.street_address(),
        "pickupCity": fake.city(),
        "pickupState": pickup_state,
        "pickupCountry": pycountry.countries.get(alpha_2=pickup_country_code).name,
        "pickupZip": fake.zipcode(),
        "pickupEmail": fake.email(),
        "rescueInst": "rescue"
    },
    "destination": {
        "destTimeTo": dest_time_to.strftime('%Y-%m-%dT%H:%M:%S'),
        "destTimeFrom": dest_time_from.strftime('%Y-%m-%dT%H:%M:%S'),
        "destPhoneNum": dest_phone_number,
        "destAddress": fake.street_address(),
        "destCountry": pycountry.countries.get(alpha_2=dest_country_code).name,
        "destCity": fake.city(),
        "destState": dest_state,
        "destZip": fake.zipcode(),
        "destEmail": fake.email(),
        "destName" : "Not Here"
    },
    "chat" : "chat...",
    "status" : "Available"
}

# Output JSON object
print(json.dumps(data, indent=4))