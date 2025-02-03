"""
! To run, please run the following command in your preferred shell

python resource/c17_mixins/example/ch1701_mixin.py

"""


class Vehicle:
    """
    Base class
    """

    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class EvMixin:
    """
    A mixin that adds more method implementation without affecting the parent's
    instantiation
    """

    name: str  # this mixin expects attribute `name` to be in the parent class

    def recharge_with_ac(self):
        assert self.name
        print(f"⚡: Recharging {self.name} with alternating current")

    def recharge_with_dc(self):
        print(f"⚡: Recharging {self.name} with direct current")


class ElectricCar(Vehicle, EvMixin):
    """
    A child class that inherits `Vehicle` and implements `EvMixin`.
    """

    def __init__(self, name: str) -> None:
        super().__init__(name)


if __name__ == "__main__":
    car = ElectricCar("my electric car")
    car.recharge_with_ac()
    car.recharge_with_dc()
