states = {
    "CA": "California",
    "NJ": "New Jersey",
    "WI": "Wisconsin",
    "NY": "New York"
}

print(states["CA"])
print(states["WI"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "Population": 395000000  # 39,500,000
    },
    "NJ": {
        "NAME": "New Jersey",
        "Population": 9000000  # 9,000,000
    },
    "WI": {
        "NAME": "Wisconsin",
        "Population": 5800000  # 5,800,000
    },
    "NY": {
        "NAME": "New York",
        "Population": 1950000  # 19,500,000
    }
}

print(nested_dictionary["CA"])
print(nested_dictionary["CA"]["Population"])
print(nested_dictionary["NY"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "Population": 395000000,  # 39,500,000
        "CITIES":[
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "NJ": {
        "NAME": "New Jersey",
        "Population": 9000000,  # 9,000,000
        "CITIES": [
            "Newark",
            "Trenton",
            "Princeton"
        ]
    },
    "WI": {
        "NAME": "Wisconsin",
        "Population": 5800000,  # 5,800,000
        "CITIES": [
            "Madison",
            "Milwaukee",
            "Green Bay"]
    },
    "NY": {
        "NAME": "New York",
        "Population": 1950000,  # 19,500,000
        "CITIES": [
            "New York City",
            "Rockester",
            "Buffalo"
        ]
    }
}
