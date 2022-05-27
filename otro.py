<<<<<<< HEAD
class Repository:
    def __init__(self):
        self.packages = {}
    def add_package(self, package):
        self.packages[package.name] = package
    def total_sice(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result
=======
class Animal:
    # sound = "Oink!"
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        name = self.name
        sound = self.sound
        return (f"{sound} I'm {name}! {sound}")


class Piglet(Animal):
    pass


class Cow(Animal):
    pass


hamlet = Piglet("Hamlet", "Oink!")
print(hamlet.speak())

milk = Cow("MilkW", "Moo!")
print(milk.speak())
>>>>>>> 5d5868d112fde3e2ad9afd7abbfc433b09d2262f
