# Base class (Parent class)
class Animals:
        def __init__(self, name):
            self.name = name  # Encapsulation: private attribute

        def speak(self):
            raise NotImplementedError("Subclass must implement abstract method")


# Derived class (Child class) - Inheritance
class Dogs(Animals):
        def speak(self):
            return f"{self.name} says Woof!"


class Cats(Animals):
        def speak(self):
            return f"{self.name} says Meow!"


# Polymorphism: Using the same method for different classes
def animal_sound(animals):
        print(animals.speak())


# Creating objects
dog = Dogs("Buddy")
cat = Cats("Whiskers")

# Calling the function with different objects
animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(cat)  # Output: Whiskers says Meow!
