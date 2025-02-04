from typing import Any


class Node:
    data: Any
    prev: "Node"
    next: "Node"

    def __init__(self, data) -> None:
        self.data = data
        self.next = None  # type: ignore
        self.prev = None  # type: ignore

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
            return f"Node({self.data}) <-> {self.next}"
        else:
            return f"Node({self.data})"

    def __repr__(self) -> str:
        return self.__str__()


class DoublyLinkedList:
    head: Node
    tail: Node

    def __init__(self, head: Node) -> None:
        self.head = head
        self.tail = self.head

    @property
    def length(self):
        if self.head is not None:
            return self.head.length
        return 0

    def push_head(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            new_head = node
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    def push_tail(self, node: Node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            new_tail = node
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

    def pop_head(self):
        if self.head:
            popped = self.head
            if self.tail == self.head:
                self.head = None  # type: ignore
                self.tail = None  # type: ignore
            else:
                self.head = self.head.next
                self.head.prev = None  # type: ignore
            popped.next = None  # type: ignore
            popped.prev = None  # type: ignore
            return popped
        raise IndexError("The Doubly Linked List is Empty")

    def pop_tail(self):
        if self.tail:
            popped = self.tail
            if self.tail == self.head:
                self.head = None  # type: ignore
                self.tail = None  # type: ignore
            else:
                self.tail = self.tail.prev
                self.tail.next = None  # type: ignore
            popped.next = None  # type: ignore
            popped.prev = None  # type: ignore
            return popped
        raise IndexError("The Doubly Linked List is Empty")

    def __str__(self) -> str:
        if self.head is None:
            return "DoublyLinkedList([])"
        return f"DoublyLinkedList([ {self.head} ])"

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    linked = DoublyLinkedList(Node(5))  # [5]
    linked.push_head(Node(4))  # [(4) <-> 5]
    linked.push_head(Node(3))  # [(3) <-> 4 <-> 5]
    linked.push_head(Node(2))  # [(2) <-> 3 <-> 4 <-> 5]
    linked.push_tail(Node(6))  # [2 <-> 3 <-> 4 <-> 5 <-> (6)]
    linked.push_tail(Node(7))  # [2 <-> 3 <-> 4 <-> 5 <-> 6 <-> (7)]

    print("Linked List:", linked)

    print(f"Popped Head: {linked.pop_head()}")  # Node(2) is popped out
    print(f"Popped Head: {linked.pop_head()}")  # Node(3) is popped out

    print("Linked List:", linked)

    print(f"Popped Tail: {linked.pop_tail()}")  # Node(7) is popped out
    print(f"Popped Tail: {linked.pop_tail()}")  # Node(6) is popped out

    print("Linked List:", linked)  # [ 4 <-> 5 ]
