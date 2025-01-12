# Advanced type hinting

# hinting lists [old method]
from typing import List

old_list: List[str] = ["old1", "old"]


# hinting lists [new method]
new_list: list[str] = ["new1", "new2"]

if __name__ == "__main__":
    print(f"old_list: {old_list}")
    print(f"new_list: {new_list }")
