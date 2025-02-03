def personify(cls):
    class Wrapped(cls):
        def set_full_name(self, full_name: str):
            self.full_name = full_name

    return Wrapped


@personify
class Animal:
    pass


animal = Animal()
animal.set_full_name("John")
print(f"The full name is: {animal.full_name}")
