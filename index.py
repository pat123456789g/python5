# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # private attribute (encapsulation)

    def make_call(self, number):
        print(f"{self.model} is calling {number}...")

    def take_photo(self):
        print(f"{self.model} took a photo 📸")

    def get_storage(self):  # Getter method (encapsulation)
        return self.__storage

    def set_storage(self, new_storage):  # Setter method
        if new_storage > 0:
            self.__storage = new_storage
        else:
            print("Invalid storage size!")

# Subclass: GamingPhone (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def take_photo(self):
        print(f"{self.model} took a high-resolution gaming-themed photo 🕹️📸")

    def play_game(self, game_name):
        print(f"Launching {game_name} on {self.model}... 🎮")

# Usage
phone1 = Smartphone("Samsung", "Galaxy S22", 128)
phone1.make_call("0712345678")
phone1.take_photo()
print("Storage:", phone1.get_storage())

gaming_phone = GamingPhone("Asus", "ROG Phone 5", 256)
gaming_phone.make_call("0798765432")
gaming_phone.take_photo()  # Polymorphism in action
gaming_phone.play_game("Call of Duty")

#activity 2
# Base class
class Animal:
    def move(self):
        pass  # abstract method

# Derived classes
class Dog(Animal):
    def move(self):
        print("Dog is running 🐕💨")

class Fish(Animal):
    def move(self):
        print("Fish is swimming 🐟🌊")

class Bird(Animal):
    def move(self):
        print("Bird is flying 🕊️☁️")

# Function that demonstrates polymorphism
def animal_move(animal):
    animal.move()

# Usage
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal_move(animal)
