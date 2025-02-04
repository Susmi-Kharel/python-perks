class Stack:
    """
    Stack is a linear data type that follows Last-In First-Out (LIFO) pattern.

    We can think a stack as a stack of biscuits on a packet or a stack of plates
    in the kitchen. The last item to add to the top of the stack will be taken
    out first to be used.

    Another good example of stack is a gift box with multiple wraps. The wrap
    that we wrapped last is always unwrapped first.

    For demonstration purpose, we create a Stack data type in python using a list.

    The basic methods in stack are:

    - length
    - push: add item to the stack
    - pop: remove item from the stack
    - peek: see the item on the top of the stack

    """

    def __init__(self):
        self.__data = []

    def __str__(self) -> str:
        return f"Stack({self.__data})"

    @property
    def length(self):
        return self.__data.__len__()

    def peek(self):
        return self.__data[-1]

    def push(self, data):
        self.__data.append(data)

    def pop(self):
        return self.__data.pop()


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)  # 1
    stack.push(2)  # 1, 2
    stack.push(3)  # 1, 2, 3
    stack.push(4)  # 1, 2, 3, 4

    print(f"Stack: {stack}")
    print(f"Peek: {stack.peek()}")  # The last item to push is peek first from the stack
    print(f"length of the Stack: {stack.length}")

    # Similarly, the first item to be popped from the stack is the last item to be pushed
    print(f"pop: {stack.pop()}")  # 4 is popped
    print(f"pop: {stack.pop()}")  # 3 is popped
    print(f"pop: {stack.pop()}")  # 2 is popped
