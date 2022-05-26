class Animal:
    #sound = "Oink!"
    def __init__(self, name):
        self.name = name
        #self.sound = sound
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