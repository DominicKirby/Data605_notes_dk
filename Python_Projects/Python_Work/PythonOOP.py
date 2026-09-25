class Animal:
    def __init__(self, name):
        self.name = name

    def eating(self):
        print(f'{self.name} is eating.')

    def speak(self): # For other child classes to this parent
        print(f"{self.name} makes a generic Animal Sound")



class Dog(Animal):  # So it inherits from super class

    # Attributes
    def __init__(self, name, age, favourite_toy): # initialise - attributes happen instantly and are saved for calling
        super().__init__(name) # Inherits name from super class
        self.age = age
        self.favourite_toy = favourite_toy
        self.__energy = 100 # Should not be easily accessed, does not come up immediately for _, or hidden completely using __
        # self.bark()

    # Behaviours
    def speak(self):
        print(f'{self.name} says Woof!')
        self.__energy -= 10

    def fetch(self):
        print(f'{self.name} brought you {self.favourite_toy}.')
        self.__energy -= 20

    def how_old(self):
        print(f'{self.name} is {self.age} years old.')

    def all_information(self):
        print(f'{self.name} is {self.age} years old and {self.favourite_toy} is their favourite toy.')

    def get_energy(self): # Getter method
        return f"{self.name} has {self.__energy} energy left" # Control how people view this

    def set_energy(self, new_energy_level): # Setter method
        if new_energy_level < 100:
            self.__energy = new_energy_level
        else:
            self.__energy = 100 # No interaction with the reader

print("-" * 20)

my_dog = Dog("Julia", 5, "a ball")
new_dog = Dog("Kenny", 7, "a stick")


"""
my_dog.speak()
my_dog.fetch()
my_dog.how_old()
my_dog.all_information()
new_dog.all_information()
"""

"""
print(my_dog.get_energy())
print("-" * 20)
my_dog.speak()
print(my_dog.get_energy())
print("-" * 20)
my_dog.fetch()
print(my_dog.get_energy())
print("-" * 20)
print("Setting energy to 95")
my_dog.set_energy(95)
print(my_dog.get_energy())
"""

my_dog.eating()

my_animal = Animal("Steve")
my_dog.speak()
my_animal.speak() # Polymorphism
