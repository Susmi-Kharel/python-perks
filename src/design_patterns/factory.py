"""
A Factory Design Pattern is a design pattern that allows user to instantiate
different object based on the constraints. In this design pattern a factory

 The components of Factory pattern are as follows:

 1. client: part of code that creates object
 2. Factory: interface that defines methods for a client code
 3. Product: it is an instance that factory creates

"""

from abc import ABC, abstractmethod
from typing import Literal


class PaymentGateway(ABC):
    """
    The PaymentGateway class is an abstract class that provides blueprint for
    all the payment methods.
    """

    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError()


class Paypal(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paid '${amount}' with paypal")


class Stripe(PaymentGateway):
    def pay(self, amount: float):
        print(f"Paid '${amount}' with stripe")


class PaymentGatewayFactory:
    """
    This is a factory class that provides the interface to instantiate a paypal
    or stripe object depending on the parameter of the `create` method.

    The create method returns the initialized object of the proper
    """

    @classmethod
    def create(cls, method: Literal["paypal", "stripe"]):
        """
        This method is a client code that initializes the respective object.
        """
        match method:
            case "paypal":
                return Paypal()
            case "stripe":
                return Stripe()
            case _:
                raise ValueError("Invalid gateway name")


if __name__ == "__main__":
    """
    here, `stripe` and `paypal` objects are products that are instantiated by
    the PaymentGatewayFactory.
    """
    stripe = PaymentGatewayFactory.create("stripe")
    stripe.pay(20)

    paypal = PaymentGatewayFactory.create("paypal")
    paypal.pay(30)
