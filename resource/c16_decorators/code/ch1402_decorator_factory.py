"""
# Decorator Factory

Decorator factory is a higher order function, that accepts arguments
"""


def moves(x: int, y: int):
    """
    This Decorator factory accepts 2 arguments which will then be used later by
    the inner function.
    """

    def factory(function):
        def inner(current_x, current_y):
            return function(current_x + x, current_y + y)

        return inner

    return factory


@moves(x=5, y=5)
def move_king(x, y):
    print(f"moved king to: {x}, {y}")


if __name__ == "__main__":
    move_king(5, 5)
