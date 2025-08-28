# smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self):
        print(f"{self.brand} {self.model} is charging... Battery at {self.battery_life}%")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage"


# Inheritance example
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system!")


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
    print(phone1)
    phone1.call("+123456789")
    phone1.charge()

    phone2 = GamingPhone("Asus", "ROG Phone 6", 256, 95, "liquid cooling")
    print(phone2)
    phone2.play_game("PUBG Mobile")
