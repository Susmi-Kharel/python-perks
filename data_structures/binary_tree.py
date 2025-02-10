from typing import Any, Literal

TraverseOrder = Literal["pre", "in", "post"]


class Node:
    value: Any
    left: "Node | None"
    right: "Node | None"

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    @property
    def size(self):
        size = 1
        if self.left:
            size += self.left.size
        if self.right:
            size += self.right.size
        return size

    def traverse(self, order: TraverseOrder = "in"):
        left = self.left.traverse(order) if self.left else None
        right = self.right.traverse(order) if self.right else None

        data = f"{self.value}"
        match order:
            case "pre":
                if left:
                    data = f"{data} -> ({left})"
                if right:
                    data = f"{data} --> ({right})"
            case "post":
                if right:
                    data = f"({right}) <- {data}"
                if left:
                    data = f"({left}) <-- {data}"
            case _:
                if left:
                    data = f"({left}) <- {data}"
                if right:
                    data = f"{data} -> ({right})"
        return data


class BinaryTree:
    """
    A Binary tree is a data type in which a parent node can have at most 2
    children. Each node contains 3 different items:

    1. data
    2. Reference to the left child
    2. Reference to the right child

    The basic methods in queue are:

    - length
    - enqueue
    - dequeue

    """

    def __init__(self, root: Node) -> None:
        self.root = root

    @property
    def size(self):
        return self.root.size

    def traverse(self, order: TraverseOrder = "in"):
        return self.root.traverse(order)


"""
Visualization
                5

        51            52

   511    512     521    522

"""

if __name__ == "__main__":
    tree = BinaryTree(Node(5))
    tree.root.left = Node(51)
    tree.root.right = Node(52)
    tree.root.left.left = Node(511)
    tree.root.left.right = Node(512)
    tree.root.right.left = Node(521)
    tree.root.right.right = Node(522)

    print(f"Size of a tree: {tree.size}")
    print(f"tree [in order]: {tree.traverse()}")
    print(f"tree [pre order]: {tree.traverse('pre')}")
    print(f"tree [post order]: {tree.traverse('post')}")

# output:

# Size of a tree: 7
# tree [in order]: ((511) <- 51 -> (512)) <- 5 -> ((521) <- 52 -> (522))
# tree [pre order]: 5 -> (51 -> (511) --> (512)) --> (52 -> (521) --> (522))
# tree [post order]: ((511) <-- (512) <- 51) <-- ((521) <-- (522) <- 52) <- 5
