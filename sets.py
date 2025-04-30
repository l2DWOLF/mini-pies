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
# List to Set to List - remove duplicates
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

students = {
    'Elsa': [90, 85, 95],
    'Anna': [89, 79 ,93],
    'Olaf': [90, 95, 97]
}

for key in students.keys():
    print(key)
for value in students.values():
    print(value)
for key, value in students.items():
    print(key, value)

for key, value in students.items():
    avg = 0
    sum = 0
    for i in range(len(value)):
        sum += value[i]
    avg = sum / len(value)
    print(f"{key}'s Average: {avg}")

students["Hans"] = [60, 70, 75]
print("New Student: ", students)
students["Christoph"] = [95, 98, 99]
students.pop("Hans")
print("Removed Hans & New Student: ", students)

word = "supercalifragilisticexpialidocious"
count = 0
for char in word:
    if char == "e":
        count += 1
print("char count: ", count)
u_chars = set(word)
print("Unique Chars: ", u_chars)

nums = [1,2,3,2,4,1,5,6,6,7]
u_nums = list(set(nums))
print("Unique Nums: ", u_nums)

for num in u_nums:
    count = 0
    for i in range(len(nums)):
        if num == nums[i]:
            count += 1
    print(f"{num}'s count: {count}")