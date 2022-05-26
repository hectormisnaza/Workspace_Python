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
material: str = ""
    def __init__(self,name):
    self.name = name
    def checkmaterial(self):
	    print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
# This Polo is made of Cotton Composition