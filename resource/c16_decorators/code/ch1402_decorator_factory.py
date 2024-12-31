"""
# Decorator Factory

Decorator factory is a higher order function, that accepts arguments
"""
import time


# ================================[ Example 1 ]================================


def log(before: bool, after: bool):
    def factory(func):
        def _inner(*args, **kwargs):
            if before:
                print(f"function execution started at: {time.time()}")
            result = func(*args, **kwargs)
            if after:
                print(f"function execution ended at: {time.time()}")
            return result

        return _inner

    return factory


@log(True, True)
def delay_execution(seconds):
    time.sleep(seconds)


# ================================[ Example 2 ]================================
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
    print(f"moved king to: ({x}, {y})")


if __name__ == "__main__":
    delay_execution(2)
    move_king(1, 1)
