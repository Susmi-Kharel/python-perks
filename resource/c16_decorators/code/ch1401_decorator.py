# ================================[ Example 1 ]================================
# raw behavior of decorator


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

# ================================[ Example 2 ]================================


def auto_typecast(fn):
    def inner(x, y):
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
