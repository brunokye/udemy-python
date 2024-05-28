"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""

from abc import ABC, abstractmethod
from random import choice


class Vehicle(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass


class LuxuryCar(Vehicle):
    def search_client(self) -> None:
        print("Luxury Car - Searching for a client...")


class PopularCar(Vehicle):
    def search_client(self) -> None:
        print("Popular Car - Searching for a client...")


class LuxuryMotorcycle(Vehicle):
    def search_client(self) -> None:
        print("Luxury Motorcycle - Searching for a client...")


class PopularMotorcycle(Vehicle):
    def search_client(self) -> None:
        print("Popular Motorcycle - Searching for a client...")


class VehicleFactory(ABC):
    def __init__(self, vehicle_type):
        self.vehicle = self.get_vehicle(vehicle_type)

    @staticmethod
    @abstractmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return PopularCar()
        elif vehicle_type == "luxurycar":
            return LuxuryCar()
        elif vehicle_type == "motorcycle":
            return PopularMotorcycle()
        elif vehicle_type == "luxurymotorcycle":
            return LuxuryMotorcycle()
        else:
            raise ValueError("Invalid vehicle type")


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "car":
            return PopularCar()
        elif vehicle_type == "luxurycar":
            return LuxuryCar()
        elif vehicle_type == "motorcycle":
            return PopularMotorcycle()
        elif vehicle_type == "luxurymotorcycle":
            return LuxuryMotorcycle()
        else:
            raise ValueError("Invalid vehicle type")


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "popular":
            return PopularCar()
        else:
            raise ValueError("Invalid vehicle type")


if __name__ == "__main__":
    available_vehicles_north_zone = [
        "car",
        "luxurycar",
        "motorcycle",
        "luxurymotorcycle",
    ]
    available_vehicles_south_zone = ["popular"]

    print("North Zone")
    for i in range(10):
        vehicle = NorthZoneVehicleFactory.get_vehicle(
            choice(available_vehicles_north_zone)
        )
        vehicle.search_client()

    print(f"\n{20 * '-'}\n")

    print("South Zone")
    for i in range(10):
        vehicle = SouthZoneVehicleFactory.get_vehicle(
            choice(available_vehicles_south_zone)
        )
        vehicle.search_client()
