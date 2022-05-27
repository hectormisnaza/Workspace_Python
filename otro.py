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
