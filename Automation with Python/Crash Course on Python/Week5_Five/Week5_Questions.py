# Instance Methods
class Dog:
    years = 0

    def dog_years(self):
        return self.years * 7


fido = Dog()
fido.years = 3
print(fido.dog_years())


""" Constructors and Other Special Methods
Problem In this code, there's a Person class that has an attribute name, which gets set when constructing the object.
Fill in the blanks so that 
1) when an instance of the class is created, the attribute gets set correctly, and 
2) when the greeting() method is called, the greeting states the assigned name."""


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("hi, my name is {}".format(self.name))


# Create a new instance with a name of your choice
some_person = Person("Héctor")
# Call the greeting method
print(some_person.greeting())


"""Inheritance
Problem: Let’s create a new class together and inherit from it. Below we have a base class called Clothing. 
Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks 
to make it work properly."""

class Clothing:
    material= ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
# This Polo is made of Cotton Composition


""" Problem: Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given 
material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts. """


class Clothing:
    stock = {'name': [], 'material': [], 'amount': []}

    def __init__(self, name):
        material = ""
        self.name = name

    def add_item(self, name, material, amount):
        Clothing.stock['name'].append(self.name)
        Clothing.stock['material'].append(self.material)
        Clothing.stock['amount'].append(amount)

    def Stock_by_Material(self, material):
        count = 0
        n = 0
        for item in Clothing.stock['material']:
            if item == material:
                count += Clothing.stock['amount'][n]
                n += 1
        return count


class shirt(Clothing):
    material = "Cotton"


class pants(Clothing):
    material = "Cotton"


polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)