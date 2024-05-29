from abc import ABC, abstractmethod


class Pizza(ABC):
    """Abstract Base Class"""

    def prepare(self) -> None:
        """Template Method"""
        self.hook()
        self.add_ingredients()
        self.cook()
        self.cut()
        self.serve()

    def hook(self) -> None:
        pass

    def cut(self) -> None:
        print(f"{self.__class__.__name__}: Cutting the pizza.")

    def serve(self) -> None:
        print(f"{self.__class__.__name__}: Serving pizza.")

    @abstractmethod
    def add_ingredients(self) -> None:
        pass

    @abstractmethod
    def cook(self) -> None:
        pass


class HouseStyle(Pizza):
    def add_ingredients(self) -> None:
        print(
            f"{self.__class__.__name__}: Adding ham, cheese and guava paste."
        )

    def cook(self) -> None:
        print(
            f"{self.__class__.__name__}: Cooking for 45 minutes in "
            "the wood burning oven."
        )


class VegetarianStyle(Pizza):
    def hook(self) -> None:
        print(f"{self.__class__.__name__}: Test.")

    def add_ingredients(self) -> None:
        print(
            f"{self.__class__.__name__}: Adding tomato sauce, cheese and "
            "basil."
        )

    def cook(self) -> None:
        print(
            f"{self.__class__.__name__}: Cooking for 30 minutes in "
            "the oven."
        )


if __name__ == "__main__":
    house_style = HouseStyle()
    house_style.prepare()

    print(f"\n{20 * '-'}\n")

    vegetarian_style = VegetarianStyle()
    vegetarian_style.prepare()
