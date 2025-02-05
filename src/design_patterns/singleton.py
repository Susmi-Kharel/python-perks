"""
Singleton Design pattern is useful when we want to initialize the object only
once. This design pattern is useful when we need to share the object state
across the whole application.

If we try to re-instantiate the new object, it always provide the previously
initialized object instead of creating the one.

The best example of the singleton design pattern is a db connection pool.
In this case, if we want to connection to the database, trying to initialize
the db connection pool always returns the same object.
"""

from datetime import datetime
from time import sleep


class ConnectionPool:
    _instance: "ConnectionPool"
    created_at: float
    name: str

    def __init__(self) -> None:
        self.created_at = datetime.now().timestamp()
        self.name = ""

    def __new__(cls):
        if hasattr(cls, "_instance"):
            print("Reusing old 'ConnectionPool' instance")
            return cls._instance
        print("Initializing new 'ConnectionPool' instance")
        cls._instance = super(ConnectionPool, cls).__new__(cls)
        return cls._instance

    @classmethod
    def _get_object(cls):
        try:
            return getattr(cls, "pool")
        except AttributeError:
            cls.pool = cls()
            return cls.pool


if __name__ == "__main__":
    pool1 = ConnectionPool()  # Initializing new 'ConnectionPool' instance
    sleep(2)

    pool2 = ConnectionPool()  # Reusing old 'ConnectionPool' instance
    sleep(2)

    pool3 = ConnectionPool()  # Reusing old 'ConnectionPool' instance

    """
    As the state of the singleton is shared across objects, changing one object
    will update the state of all instantiated objects.
    """
    print(pool1.created_at)
    print(pool2.created_at)  # created timestamp will be same
    print(pool3.created_at)  # created timestamp will be same

    pool2.name = "Pool 2"

    print(pool1.name)  # Pool 2
    print(pool3.name)  # Pool 2
