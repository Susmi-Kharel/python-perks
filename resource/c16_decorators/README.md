# Chapter 16: Decorators

> **Note**:
>
> please refer to the repository
> **[python projects](https://github.com/ghimiresdp/python-projects)** for more
> exercises and projects related to this chapter.

**Table of contents**:
- [Chapter 16: Decorators](#chapter-16-decorators)
- [Introduction to decorators](#introduction-to-decorators)
- [decorator factories](#decorator-factories)
- [class based decorators](#class-based-decorators)


# Introduction to decorators

Decorators are higher order functions that accept functions or callables as
arguments, modifies it's base behavior, and finally returns the same callable by
updating the arguments accordingly.

**The raw behavior of decorator is shown in the code below**:

```python
def decorate_me(func):
    def inner(*args, **kwargs):
        print("This is first called before executing the original method")
        return func(*args, **kwargs)

    return inner


def original_method():
    print("This is an original method")


decorated = decorate_me(original_method)
print("Calling Decorated method: ")
decorated()
```

### output

```
Calling Decorated method:
This is first called before executing the original method
This is an original method
```

To avoid creating a new `calable` identifier named `decorated` and calling it,
we can use `@` annotation to define it as a decorator so that we can directly
use`original_method()` instead.

```diff
+ @decorate_me
def original_method():
    print("This is an original method")

- decorated = decorate_me(original_method)
print("Calling Decorated method: ")
- decorated()

+ original_method()

```

Decorator pattern is a well-known design pattern in programming language that
helps us utilizing the same feature along multiple functions without changing
each functions repeatedly.

For example, we have 2 functions, `add` and `subtract`, that can subtract only
numeric values, however if we want to be able to subtract a number string from
another, then we might first need to check if the parameters can be converted to
number or not. However, this process needs to be repeated for all the methods
like `add` and `subtract`. To avoid such repetition, we can introduce a new
decorator that checks these conditions and automatically typecast values to it.

```python
def auto_typecast(fn):
    def inner(x: str, y):
        if isinstance(x, str):
            x = int(x)
        if isinstance(y, str):
            y = int(y)
        return fn(x, y)

    return inner


@auto_typecast
def add(x, y):
    return x + y


@auto_typecast
def subtract(x, y):
    return x - y


if __name__ == "__main__":
    print("adding number 5 and string '6': ", add(5, "6"))
    print("subtracting number 5 from string '10': ", subtract("10", 5))

```

# decorator factories

Sometimes, we might need to configure the decorated method with different
arguments. For example, We might have different conditions to log the timing
of different methods.

In such scenario, decorator factory is useful. decorator factory uses one more
level of decorated function that accepts argument so that same decorator can be
used at multiple places with multiple behaviors.

For example:

```python
import time

def log(before: bool, after: bool):
    def factory(func):
        def _inner(*args, **kwargs):
            if before:
                print(f"function {func} execution started at: {time.time()}")
            result = func(*args, **kwargs)
            if after:
                print(f"function {func} execution ended at: {time.time()}")
            return result

        return _inner

    return factory


@log(True, True)
def delay_execution(seconds):
    time.sleep(seconds)

@log(before=True, after=False)
def print_hello():
    print("Hello")


delay_execution(2)
print_hello()

```

### Output

```
function <function delay_execution at 0x0000021614B2E200> execution started at: 1735680038.99797
function <function delay_execution at 0x0000021614B2E200> execution ended at: 1735680040.9992893
function <function print_hello at 0x0000021614B2E340> execution started at: 1735680040.9992893
Hello
```

# class based decorators

Class based decorators are decorators that behave similar to functional
decorators, however they are created using classes. It uses special methods
`__init__`, and `__call__` to accomplish similar behavior.

Example:

```python
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

regular_function()
```

### output
```
the function regular_function is being called
this is a function body
the function regular_function has been successfully called
```
