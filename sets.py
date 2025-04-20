
riverbank = {"Pool", "24/7 Doorman", "Fitness Center", 
             "Grilling Stations", "Resident Lounge"}
henryhall = {"W/D in unit", "24/7 Doorman", "Fitness Center",
             "Music Room", "Bar", "Resident Lounge"}
thelandon = {"Rooftop Lounge", "24/7 Doorman", "Fitness Center",
             "Screening Room", "Resident Lounge", "Pool"}

# .union(riverbank)
all_amenities = riverbank|henryhall|thelandon 
print("All Amenities: \n", all_amenities)

# .intersection(riverbank)
intersections = riverbank&henryhall&thelandon
print("InterSections: \n", intersections)

# .difference(riverbank)
diff_amenities = riverbank - henryhall - thelandon
print("Unique: \n", diff_amenities)

# .symetric_difference(riverbank) 
symetric_diff = riverbank ^ henryhall ^ thelandon
print("Symetric diff: \n", symetric_diff)

# Set to List
buildings = list(riverbank | henryhall | thelandon)
buildings.append("Concierge")
print(buildings)

# List to Set to List without duplicates
duplist = [1,1,2,2,3,3,4,5,6,7]
duplist = list(set(duplist))
print(duplist)

