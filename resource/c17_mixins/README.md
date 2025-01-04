# Chapter 17: Mixins

**Table of contents**:
- [Chapter 17: Mixins](#chapter-17-mixins)
  - [Introduction to mixin](#introduction-to-mixin)
    - [Example of a mixin](#example-of-a-mixin)


## Introduction to mixin

Mixin is a class that adds method implementation. It is intended to be used to
add method implementation but not instantiation so we generally add methods to
the mixin class. Mixin uses a concept of multiple inheritance to combine all
parent methods to create a new type by a child class.

We can implement multiple mixins in a child class to expand its usability and
reduce code duplication. Python uses `C3 Linearization` or
`Method Resolution order` to deal with collisions if there are same methods
defined in multiple mixins. To know more about it, you can review the topic
`Multiple Inheritance`.

Reference: <https://en.wikipedia.org/wiki/C3_linearization>

### Example of a mixin
```python
# resource/c17_mixins/example/ch1501_mixin.py
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

```

**Output**
```
⚡: Recharging my electric car with alternating current
⚡: Recharging my electric car with direct current
```
