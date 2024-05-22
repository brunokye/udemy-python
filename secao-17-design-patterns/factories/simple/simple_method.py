"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
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
    @staticmethod
    def get_vehicle(vehicle_type: str) -> Vehicle:
        if vehicle_type == "popular":
            return PopularCar()
        elif vehicle_type == "luxury":
            return LuxuryCar()
        elif vehicle_type == "motorcycle":
            return PopularMotorcycle()
        elif vehicle_type == "luxurymotorcycle":
            return LuxuryMotorcycle()
        else:
            raise ValueError("Invalid vehicle type")


if __name__ == "__main__":
    available_vehicles = [
        "popular",
        "luxury",
        "motorcycle",
        "luxurymotorcycle",
    ]

    for i in range(10):
        vehicle = VehicleFactory.get_vehicle(choice(available_vehicles))
        vehicle.search_client()
