"""Practice Notebook: Methods and Classes
The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that
are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors
requested."""


class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        return f"Current floor: {self.current}"

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current += 1

    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > 0:
            self.current -= 1

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= self.bottom and floor <= self.top:
            self.current = floor
        elif floor < 0:
            self.current = 0
        else:
            self.current = 10


elevator = Elevator(-1, 10, 0)

"""This class is pretty empty and doesn't do much. To test whether your Elevator class is working correctly, run the 
code blocks below."""

elevator.up()
elevator.current  # should output 1

elevator.down()
elevator.current  # should output 0

elevator.go_to(10)
elevator.current  # should output 10

"""If you get a NameError message, be sure to run the Elevator class definition code block first. If you get an 
AttributeError message, be sure to initialize self.current in your Elevator class.

Once you've made the above methods output 1, 0 and 10, you've successfully coded the Elevator class and its methods. 
Great work!

For the up and down methods, did you take into account the top and bottom floors? Keep in mind that the elevator 
shouldn't go above the top floor or below the bottom floor. To check that out, try the code below and verify if it's 
working as expected. If it's not, then go back and modify the methods so that this code behaves correctly."""

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)  # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current)  # should be 1

"""Now add the str method to your Elevator class definition above so that when printing the elevator using the print( ) 
method, we get the current floor together with a message. For example, in the 5th floor it should say 
'Current floor: 5'"""

elevator.go_to(5)
print(elevator)


#Code Reuse
"""Let’s put what we learned about code reuse all together.
First, let’s look back at inheritance. Run the following cell that defines a generic Animal class."""


class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category

"""What we have is not enough to do much -- yet. That’s where you come in.
In the next cell, define a Turtle class that inherits from the Animal class. Then go ahead and set its category. 
For instance, a turtle is generally considered a reptile. Although modern cladistics call this categorization into 
question, for purposes of this exercise we will say turtles are reptiles!"""

class Turtle(Animal):
    category = "reptile"

"""Run the following cell to check whether you correctly defined your Turtle class and set its category to reptile."""

print(Turtle.category)

"""Was the output of the above cell reptile? If not, go back and edit your Turtle class making sure that it inherits 
from the Animal class and its category is properly set to reptile. Be sure to re-run that cell once you've finished 
your edits. Did you get it? If so, great!

Next, let’s practice composition a little bit. This one will require a second type of Animal that is in the same 
category as the first. For example, since you already created a Turtle class, go ahead and create a Snake class. 
Don’t forget that it also inherits from the Animal class and that its category should be set to reptile."""

class Snake(Animal):
    category = "reptile"

"""Now, let’s say we have a large variety of Animals (such as turtles and snakes) in a Zoo. Below we have the Zoo class.
 We’re going to use it to organize our various Animals. Remember, inheritance says a Turtle is an Animal, but a Zoo 
 is not an Animal and an Animal is not a Zoo -- though they are related to one another.

Fill in the blanks of the Zoo class below so that you can use zoo.add_animal( ) to add instances of the Animal 
subclasses you created above. Once you’ve added them all, you should be able to use zoo.total_of_category( ) to 
tell you exactly how many individual Animal types the Zoo has for each category! Be sure to run the cell once you've 
finished your edits."""


class Zoo:
    def __init__(self):
        self.current_animals = {}

    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()


"""Run the following cell to check whether you properly filled in the blanks of your Zoo class."""


turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category


"""Was the output of the above cell 2? If not, go back and edit the Zoo class making sure to fill in the blanks with 
the appropriate attributes. Be sure to re-run that cell once you've finished your edits.

Did you get it? If so, perfect! You have successfully defined your Turtle and Snake subclasses as well as your 
Zoo class. You are all done with this notebook. Great work!"""