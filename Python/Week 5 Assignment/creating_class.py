# Base Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # calling parent constructor
        self.__storage = storage  # Encapsulation: private attribute
        self.os = os

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.device_info()} 📲")

    def get_storage(self):
        return f"Available storage: {self.__storage}GB"

    def use_storage(self, amount):
        if amount <= self.__storage:
            self.__storage -= amount
            print(f"{amount}GB used. {self.__storage}GB left.")
        else:
            print("Not enough storage!")


# Creating Objects
phone1 = Smartphone("Apple", "iPhone 14", "iOS", 128)
phone2 = Smartphone("Samsung", "Galaxy S23", "Android", 256)

# Using methods
print(phone1.device_info())
phone1.install_app("WhatsApp")
phone1.use_storage(20)
print(phone1.get_storage())

print("\n--- Another Phone ---")
print(phone2.device_info())
phone2.install_app("Instagram")
