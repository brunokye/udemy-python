"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""

from abc import ABC, abstractmethod


class PopularVehicle(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass


class LuxuryVehicle(ABC):
    @abstractmethod
    def search_client(self) -> None:
        pass


class PopularCarNZ(PopularVehicle):
    def search_client(self) -> None:
        print("Popular Car NZ - Searching for a client...")


class LuxuryCarNZ(LuxuryVehicle):
    def search_client(self) -> None:
        print("Luxury Car NZ - Searching for a client...")


class PopularMotorcycleNZ(PopularVehicle):
    def search_client(self) -> None:
        print("Popular Motorcycle NZ - Searching for a client...")


class LuxuryMotorcycleNZ(LuxuryVehicle):
    def search_client(self) -> None:
        print("Luxury Motorcycle NZ - Searching for a client...")


class PopularCarSZ(PopularVehicle):
    def search_client(self) -> None:
        print("Popular Car SZ - Searching for a client...")


class LuxuryCarSZ(LuxuryVehicle):
    def search_client(self) -> None:
        print("Luxury Car SZ - Searching for a client...")


class PopularMotorcycleSZ(PopularVehicle):
    def search_client(self) -> None:
        print("Popular Motorcycle SZ - Searching for a client...")


class LuxuryMotorcycleSZ(LuxuryVehicle):
    def search_client(self) -> None:
        print("Luxury Motorcycle SZ - Searching for a client...")


class VehicleFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_car() -> PopularVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_luxury_car() -> LuxuryVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_motorcycle() -> PopularVehicle:
        pass

    @staticmethod
    @abstractmethod
    def get_luxury_motorcycle() -> LuxuryVehicle:
        pass


class NorthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_car() -> PopularVehicle:
        return PopularCarNZ()

    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarNZ()

    @staticmethod
    def get_motorcycle() -> PopularVehicle:
        return PopularMotorcycleNZ()

    @staticmethod
    def get_luxury_motorcycle() -> LuxuryVehicle:
        return LuxuryMotorcycleNZ()


class SouthZoneVehicleFactory(VehicleFactory):
    @staticmethod
    def get_car() -> PopularVehicle:
        return PopularCarSZ()

    @staticmethod
    def get_luxury_car() -> LuxuryVehicle:
        return LuxuryCarSZ()

    @staticmethod
    def get_motorcycle() -> PopularVehicle:
        return PopularMotorcycleSZ()

    @staticmethod
    def get_luxury_motorcycle() -> LuxuryVehicle:
        return LuxuryMotorcycleSZ()


class Client:
    def search_clients(self):
        for factory in [NorthZoneVehicleFactory, SouthZoneVehicleFactory]:
            car = factory.get_car()
            car.search_client()

            luxury_car = factory.get_luxury_car()
            luxury_car.search_client()

            motorcycle = factory.get_motorcycle()
            motorcycle.search_client()

            luxury_motorcycle = factory.get_luxury_motorcycle()
            luxury_motorcycle.search_client()


if __name__ == "__main__":
    client = Client()
    client.search_clients()
