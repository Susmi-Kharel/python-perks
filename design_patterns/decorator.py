"""
A decorator design pattern is a structural design pattern that allows to
dynamically attach new behavior to the existing object without changing the
original implementation.

A decorator creates a wrapper around the original implementation so that it can
be reused in another implementation too.

We can implement decorator pattern where we want some conditional results such
as displaying logs while debugging.
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class PrivateProfileDecorator:
    def __init__(self, user: User) -> None:
        self.user = user

    def display(self):
        print(f"[Private Profile] Name: {self.user.name}")


class PublicProfileDecorator:
    def __init__(self, user: User) -> None:
        self.user = user

    def display(self):
        print(f"[Public Profile] Name: {self.user.name}, age: {self.user.age}")


"""
In python, we can also use functional decorators to work on a decorator pattern.
A basic logger with decorator design pattern is as follows:
"""


def logger(func):
    def __inner(*args, **kwargs):
        print(f"[ LOG ] calling function [{func.__name__}]")
        return func(*args, **kwargs)

    return __inner


@logger
def add(x: int, y: int):
    print(f"The sum is: {x+y}")


if __name__ == "__main__":
    user = User("John Doe", 20)

    private = PrivateProfileDecorator(user)
    private.display()

    public = PublicProfileDecorator(user)
    public.display()

    # logger decorated add function
    add(5, 10)
    """
    OUTPUT:

    [Private Profile] Name: John Doe
    [Public Profile] Name: John Doe, age: 20

    [ LOG ] calling function [add]
    The sum is: 15
    """
