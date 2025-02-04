class Node:
    next: "Node"

    def __init__(self, data) -> None:
        self.data = data
        self.next = None  # type: ignore

    def push(self, node: "Node"):
        if self.length > 1:
            self.next.push(node)
        else:
            self.next = node

    def pop(self):
        match self.length:
            case 1:
                return None
            case 2:
                popped = self.next
                self.next = None  # type: ignore
                return popped
            case _:
                return self.next.pop()

    @property
    def length(self):
        if self.next is not None:
            return 1 + self.next.length
        return 1

    def __str__(self) -> str:
        if self.length > 1:
            return f"Node({self.data}) -> {self.next}"
        else:
            return f"Node({self.data})"

    def __repr__(self) -> str:
        return self.__str__()


class LinkedList:
    head: Node

    def __init__(self, head: Node) -> None:
        self.head = head

    @property
    def length(self):
        if self.head is not None:
            return self.head.length
        return 0

    def push(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            self.head.push(node)

    def pop(self):
        match self.length:
            case 0:
                raise IndexError("The linked list is Empty")
            case 1:
                popped = self.head
                self.head = None  # type: ignore
                return popped
            case _:
                return self.head.pop()

    def __str__(self) -> str:
        if self.head is None:
            return "LinkedList([])"
        return f"LinkedList([ {self.head} ])"

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    linked = LinkedList(Node(5))
    linked.push(Node(2))
    linked.push(Node(7))
    linked.push(Node(3))
    linked.push(Node(8))
    print("Linked List:", linked)
    print(f"Popped: {linked.pop()}")  # Node(8) is popped out
    print(f"Popped: {linked.pop()}")  # Node(3) is popped out
    print(f"Popped: {linked.pop()}")  # Node(7) is popped out
    print(f"Popped: {linked.pop()}")  # Node(2) is popped out
    print(f"Popped: {linked.pop()}")  # Node(5) is popped out

    try:
        linked.pop()
    except IndexError as e:
        print(f"error: {e}")  # The linked list is Empty
