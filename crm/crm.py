# from pyscript import document

class Client:
# Constructor 
    def __init__(self, first_name, last_name, email, 
    budget, move_date, notes):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.budget = budget
        self.move_date = move_date
        self.notes = notes
# Methods
    def __str__(self):
        return f"{self.first_name}'s Profile: \nName: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}, Budget: {self.budget}, Move in Date: {self.move_date}, Notes: {self.notes}"
    def print_client(self):
        return f"{self.first_name}'s Profile: \n{self.first_name}, {self.last_name}, {self.email}, {self.budget}, {self.move_date}, {self.notes}"
    def update_client(self, arg):
        self.budget = arg


p = Client("John", "Fitzpatrick", "John_F@gmail.com", 4300, "August 15", "W/D in unit, Pet Friendly.")
print(p.budget)
print(p.print_client())
p.update_client(5000)
print(p)

for key,value in p:
    print(f"\nKey {key}, value {value}")

""" clientp = document.createElement('p')
clientp.textContent = p
document.body.appendChild(clientp) """
