The three programs are used to create test JSON data. The data populates the 
following JSON scheme.

    data = {
        "shippersPO": "",
        "paymentTerms": "",
        "paymentType": "",
        "offerAmt": "",
        "numOfPackages": "",
        "deliveryDistMiles": "",
        "deliveryTimeMin": "",
        "pickup": {
            "pickupTimeTo": "",
            "pickupTimeFrom": "",
            "pickupName": "",
            "pickupPhoneNum": "",
            "pickupAddress": "",
            "pickupCity": "",
            "pickupState": "",
            "pickupCountry": "",
            "pickupZip": "",
            "pickupEmail": "",
            "rescueInst": "",
            "pickupLatitude" : "",
            "pickupLongitude" : "",
        },
        "destination": {
            "destTimeTo": "",
            "destTimeFrom": "",
            "destPhoneNum": "",
            "destAddress": "",
            "destCountry": "",
            "destCity": "",
            "destState": "",
            "destZip": "",
            "destEmail": "",
            "destName" : "",
            "destLatitude" : "",
            "destLongitude" : "",
        },
        "chat" : "Python generator...",
        "status" : "Available"
    }

DeliveryJSONFake.py
This program uses only fake data and generates only 1 entry.

DeliveryReal.py
This program uses some real and some fake data. The address information is real.
The distance is the actual linear distance between the pickup and destination.
Other stuff like name and offer ammount are fake.

DeliveryPackagesReal.py
This program added delivery package data.
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
