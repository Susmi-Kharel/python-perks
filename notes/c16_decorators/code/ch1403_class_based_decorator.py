from typing import Any, Callable


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f"the function {self.func.__name__} is being called")
        result = self.func(*args, **kwds)
        print(f"the function {self.func.__name__} has been successfully called")
        return result


@LoggerDecorator
def regular_function():
    print("this is a function body")


if __name__ == "__main__":
    regular_function()
