class Queue:
    """
    A queue is a linear data type that follows First-In First-Out (FIFO) pattern.

    There is already a built-in queue data type in python, however for
    demonstration purpose, we create a Queue data type in python using a list.

    The basic methods in queue are:

    - length
    - enqueue
    - dequeue

    """

    def __init__(self):
        self.__data = []

    def __str__(self) -> str:
        return f"Queue({self.__data})"

    @property
    def length(self):
        return self.__data.__len__()

    def enqueue(self, data):
        self.__data.insert(0, data)

    def dequeue(self):
        return self.__data.pop()


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)  # 1
    queue.enqueue(2)  # 2, 1
    queue.enqueue(3)  # 3,2,1
    queue.enqueue(4)  # 4,3,2,1

    print(f"Queue: {queue}")
    print(f"length of queue: {queue.length}")

    print(f"dequeue: {queue.dequeue()}")  # 1 is popped
    print(f"dequeue: {queue.dequeue()}")  # 2 is popped
    print(f"dequeue: {queue.dequeue()}")  # 3 is popped
