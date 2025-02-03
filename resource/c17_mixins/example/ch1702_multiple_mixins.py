"""
! To run, please run the following command in your preferred shell

python resource/c17_mixins/example/ch1702_multiple_mixins.py

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


class GasolineMixin:
    """
    Something similar to EvMixin, but with other method implementation
    """

    MAX_VOLUME: int
    fuel_available: int

    def refuel(self, volume: int):
        new_volume = self.fuel_available + volume
        if new_volume > self.MAX_VOLUME:
            print(f"Overflow: {new_volume - self.MAX_VOLUME}")
            self.fuel_available = self.MAX_VOLUME
        else:
            self.fuel_available = new_volume


class HybridCar(Vehicle, EvMixin, GasolineMixin):
    """
    A child class that inherits `Vehicle` and implements `EvMixin`.
    """

    MAX_VOLUME = 50

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.fuel_available = 0


if __name__ == "__main__":
    car = HybridCar("my electric car")
    car.refuel(60)  # Overflow: 10
    car.recharge_with_ac()  # ⚡: Recharging my electric car with alternating current
