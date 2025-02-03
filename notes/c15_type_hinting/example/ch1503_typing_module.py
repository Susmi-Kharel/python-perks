# Advanced type hinting using typing module
# This is useful for python version below 3.10

from typing import List, Literal, TypedDict, Union

my_list: List[Union[int, str]] = ["John", "Jane", 2]


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
