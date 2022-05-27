"""Classes and Methods
Instance Methods
Problem OK, now it’s your turn! Have a go at writing methods for a class. Create a Dog class with dog_years based on
the Piglet class shown before (one human year is about 7 dog years)."""


# example 1
class Piglet():
    def speak(self):
        print("oink oink")


hamlet = Piglet()
hamlet.speak()


# example 2  Instance Methods
class Piglet():
    name = ""

    def speak(self):
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


jonagold = Apple("red", "sweet")

print(f"My color is {jonagold.color}, and my flavor is {jonagold.flavor}")
print(jonagold)


#  Object Inheritance

class Animal:
    sound = "Oink!"

    def __init__(self, name):
        self.name = name
        # self.sound = sound

    def speak(self):
        return ("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))


class Piglet(Animal):
    sound = "Oink!"


hamlet = Piglet("Hamlet")
print(hamlet.speak())


class Cow(Animal):
    sound = "Moo"


milk = Cow("MilkW")
print(milk.speak())


# otro ejemplo donde los atributos van desde el metodo constructor

class Animal:
    def __init__(self, name, sound, animal):
        self.name = name
        self.sound = sound
        self.animal = animal

    def speak(self):
        name = self.name
        sound = self.sound
        animal = self.animal
        return (f"{sound} Hi, I'm {name}! {sound}, I'm a {animal}")


class Piglet(Animal):
    pass


class Cow(Animal):
    pass


hamlet = Piglet("Hamlet", "Oink!", "Pig")
print(hamlet.speak())

milk = Cow("MilkW", "Moo!", "Cow")
print(milk.speak())

milk = Cow("MilkW", "", "Cow")
print(milk.speak())

# Classes and Methods
"""Inheritance"""


class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.color, granny_smith.flavor)
print(carnelian.color, carnelian.flavor)
<<<<<<< HEAD
=======

>>>>>>> 5d5868d112fde3e2ad9afd7abbfc433b09d2262f
