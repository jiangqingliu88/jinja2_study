class Dog:
    """A simple dog class"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class Cat:
    """A simple cat class"""

    def speak(self):
        return "Meow!"

    def __str__(self):
        return "Cat"
    
class DogFactory:
    """Concrete dog factory"""

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"

class CatFactory:
    """Concrete cat factory"""

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"

class PetStore:
    """Petstore housing our factories"""

    def __init__(self, pet_factory=None):
        """pet_factory is our abstract factory.
        We can set it at runtime.
        """

        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects retured by the factory"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

#Create a concrete factory
factory = DogFactory()

#Create a pet store housing our Dog Factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()
