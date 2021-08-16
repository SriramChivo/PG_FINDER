import datetime
from django.db import models


class PgChoices:

    men = "men"
    ladies = "ladies"
    unisex = "unisex"

    choices = [
        (men, "Men"),
        (ladies, "ladies"),
        (unisex, "unisex")
    ]


class PgLocationChoices:

    cities = [
        ("Bangalore", "Bangalore"),
        ("Chennai", "Chennai"),
        ("Coimbatore", "Coimbatore"),
        ("Chandigarh", "Chandigarh"),
        ("Delhi", "Delhi"),
        ("Gurugoan", "Gurugoan"),
        ("Hyderabad", "Hyderabad"),
        ("Kolkata", "Kolkata"),
        ("Kochi", "Kochi"),
        ("Mangalore", "Mangalore"),
        ("Mumbai", "Mumbai"),
        ("Mysuru", "Mysuru"),
        ("Noida", "Noida"),
        ("Trivandrum", "Trivandrum"),
        ("Vizag", "Vizag")
    ]
