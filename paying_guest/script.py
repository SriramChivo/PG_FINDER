from .models import Amenities

bro = [("Not Set", "Not Set"), ('Uninterrupted Power Supply', 'Uninterrupted Power Supply'), ('24/7 Water Supply', '24/7 Water Supply'), ('UPS Backup', 'UPS Backup'), ('3 Times Food in weekdays', '3 Times Food in weekdays'), ('Sunday Non Veg', 'Sunday Non Veg'), ('2 Times Food in weekdays',
                                                                                                                                                                                                                                                                        '2 Times Food in weekdays'), ('Hygenic Home Cooking', 'Hygenic Home Cooking'), ('Daily Cleaning Maintenance', 'Daily Cleaning Maintenance'), ('24/7 Washing Machine Supply', '24/7 Washing Machine Supply'), ('Hot Water Supply', 'Hot Water Supply'), ('Parking Facilty', 'Parking Facilty')]

j = [Amenities(name=each[0]) for each in bro]
Amenities.objects.bulk_create(j)
