# Advanced type hinting with less typing module
# This is useful for python version greater than or equal to 3.10

from typing import Literal, TypedDict

my_list: list[int | str] = ["John", "Jane", 2]


class User(TypedDict):
    id: int
    name: str
    type: Literal["admin", "staff"]


if __name__ == "__main__":
    print(f"My List: {my_list }")

    user: User = {
        "id": 1,
        "name": "John Doe",
        "type": "admin",
    }
    print(user)
