from utils import color_prt as cp
riverbank = {"Pool", "24/7 Doorman", "Fitness Center", 
             "Grilling Stations", "Resident Lounge"}
henryhall = {"W/D in unit", "24/7 Doorman", "Fitness Center",
             "Music Room", "Bar", "Resident Lounge"}
thelandon = {"Rooftop Lounge", "24/7 Doorman", "Fitness Center",
             "Screening Room", "Resident Lounge", "Pool"}

dict1 = {}
dict2 = dict()
dict3 = dict(key="value", key2="value2", num=3)

river_object = {
    "amenities": riverbank,
    "address": "560 West 43rd Street"
}
henry_object = {
    "amenities": henryhall,
    "address": "515 West 38th Street"
}
landon_object = {
    "amenities": list(thelandon),
    "address": "520 West 43rd Street"
}

print("\n",landon_object["address"], landon_object["amenities"], "\n")

for key in henry_object.keys():
    print('key: ', key)
for value in henry_object.values():
    print('val: ',value)
print('\n')

for key, value in river_object.items():
    landon_object[key+" river's"] = value
print("landon+river Object: ", landon_object)

print(f"\033[96m")
# .union(riverbank)
all_amenities = riverbank|henryhall|thelandon 
print("All Amenities: \n", all_amenities)
print(f"\033[0m")

print(f"\033[95m")
# .intersection(riverbank)
intersections = riverbank&henryhall&thelandon
print("InterSections: \n", intersections)
print(f"\033[0m")

print(f"\033[91m")
# .difference(riverbank)
diff_amenities = riverbank - henryhall - thelandon
print("Unique: \n", diff_amenities)
print(f"\033[0m")

print(f"\033[94m")
# .symetric_difference(riverbank) 
symetric_diff = riverbank ^ henryhall ^ thelandon
print("Symetric diff: \n", symetric_diff)
print(f"\033[0m")

print(f"\033[92m")
# Set to List
buildings = list(riverbank | henryhall | thelandon)
buildings.append("Concierge")
print(buildings)
print(f"\033[0m")

print(f"\033[90m")
# List to Set to List without duplicates
duplist = [1,1,2,2,3,3,4,5,6,7]
duplist = list(set(duplist))
print(duplist, end= "", flush=True)
print(f"\033[0m")

pet_dict = {
    "name": "Ray",
    "age": 17.14286,
    "type": "Dog",
    "status": "Happy", 
    "phrase": "Forver until proven otherwise"
}

key = "age"
if key in pet_dict:
    print(cp.print(
        "cyan", f"❤️❤️❤️    Age: {round(pet_dict[key])}, Human Age: {pet_dict[key]*7:.4f} ❤️❤️❤️"))
if "birthday" not in pet_dict:
    pet_dict["birthday"] = "August 15th"
for key, value in pet_dict.items():
    print(key,":", value)