"""Classes and Methods
Instance Methods
Problem OK, now it’s your turn! Have a go at writing methods for a class. Create a Dog class with dog_years based on
the Piglet class shown before (one human year is about 7 dog years)."""

#example 1
class Piglet():
    def speak(self):
        print("oink oink")

hamlet = Piglet()
hamlet.speak()

# example 2  Instance Methods
class Piglet():
    # name = ""
    def speak(self):
        # print(self.__getattribute__("name"))
        print("oink! I'm {}! Oink".format(self.name))
        return ("oink!  oink!")
    def years(self):
        return self.year * 18


brave = Piglet()
brave.name = "Valiente"
brave.speak()
brave.year = 2
print(brave.years())

mike = Piglet()
mike.name = "Mike"
mike.speak()
mike.year = 1.5
print(f"My name is {mike.name}, tengo {mike.years()}, y hago:{mike.speak()}")

# Constructors and Other Special Methods

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}.".format(self.color, self.flavor)


jonagold = Apple("red","sweet")

print(f"My color is {jonagold.color}, and my flavor is {jonagold.flavor}")
print(jonagold)

"""Inheritance
Problem: Let’s create a new class together and inherit from it. Below we have a base class called Clothing. 
Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks 
to make it work properly."""

class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))

class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
This Polo is made of Cotton
Composition

""" Problem: Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts. """

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"

polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)